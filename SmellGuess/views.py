#-*- coding: utf-8 -*-

"""
Authors : 
- Arnaud Ferré, arnaud.ferre.pro@gmail.com (2014)
- Jean Coquet, public@jeancoquet.com (2014)
"""


################################################################
#######################    LIBRARIES    ########################
################################################################
# Django libs:
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from django.core.servers.basehttp import FileWrapper
from django.utils.encoding import smart_str, smart_unicode 
from django.utils.translation import ugettext_lazy as _

# External libs:
from datetime import datetime
import random
import time
import codecs
import os, tempfile, zipfile
from base64 import decodestring

# Local import:
from forms import SmellerModelForm, SmellerModelForm2
from SmellGuess.models import Smeller, Sample, Guess, Image, Humor, Note


################################################################
#########################    VIEWS    ##########################
################################################################

def homeView(request):
    """Called view by the URL /home.

    No particular parameters. The homepage is just a static page.

    Parameters
    ----------
    request : HttpRequest object
        Contain many info (GET/POST method, forms data, session data, ...).

    Returns
    -------
    render() : HttpResponse object
        The render() function contain 3 parameters:
            1) Initial request
            2) Path of a template
            3) A dictionary which contains all data accessible in the template (before generation) 
        This function generates an HTML file after analyzing the correct template.

    Examples
    --------

    See also
    --------

    Notes
    -----

    TODO: delete all data in var and delete data from uncomplete game
    TODO: See serialization of session var (https://docs.djangoproject.com/en/1.7/topics/http/sessions/)

    """
    
    # RE-Initialization of variable of session (use during all the session):
    request.session['idSmeller'] = None
    request.session['currentIdGuess'] = None
    request.session['guessStep'] = None
    request.session['SampleIdToAnalyze'] = None
    request.session['guessStep'] = None #To adapt the demo mode for game part
    
    paramToGenerateTemplate = dict()
    if 'demoMode' not in request.session.keys():
        request.session['demoMode'] = True #init in demo mode
    
    paramToGenerateTemplate['demoMode'] = request.session['demoMode']
        
    # Render:    
    return render(request, 'SmellGuessTemplate/home.html', paramToGenerateTemplate)#{'nb': nb, 'intensity': intensity, 'color': color, 'note': note, 'image': image, 'opacity': opacity, 'name': name})        




def registrationView(request):
    """Called view by the URL /registration/.

    No particular parameters. The registration page is just a static page.
    It contains form.

    Parameters
    ----------
    request : HttpRequest object
        Contain many info (GET/POST method, forms data, session data, ...).

    Returns
    -------
    render() : HttpResponse object
        The render() function contain 3 parameters:
            1) Initial request
            2) Path of a template
            3) A dictionary which contains all data accessible in the template (before generation) 
        This function generates an HTML file after analyzing the correct template.

    Examples
    --------

    See also
    --------

    Notes
    -----

    """
        
    form = SmellerModelForm()
    form2 = SmellerModelForm2()
    
    return render(request, 'SmellGuessTemplate/registration.html', {'current_date': datetime.now(), 'form': form, 'form2': form2})




def getAllId(l_objects):
    l_allId = list()   
    for obj in l_objects:
        l_allId.append(obj.id)
    return l_allId

def getAllName(l_id, objectType):
    l_allObject = list()   
    for currentId in l_id:
        l_allObject.append(objectType.get(id=currentId).name)
    return l_allObject

def gameView(request):
    """Called view by the URL /game.

    An unique view is called for all processes of the game.

    Parameters
    ----------
    request : HttpRequest object
        Contain many info (GET/POST method, forms data, session data, ...).

    Returns
    -------
    render() : HttpResponse object
        The render() function contain 3 parameters:
            1) Initial request
            2) Path of a template
            3) A dictionary which contains all data accessible in the template (before generation) 
        This function generates an HTML file after analyzing the correct template.

    Examples
    --------

    See also
    --------

    Notes
    -----
    TODO: Use var in URL to generate a specific game page

    """
    
    paramToGenerateTemplate = dict()
    
    if request.method == 'POST':
        
        ### FIRST CONNECTION: ###
        # If Smeller is not registrated = first visit of user on game page
        if request.session['idSmeller'] == None : 
            
            formSmeller = SmellerModelForm(request.POST)  # then data is collected.
            if formSmeller.is_valid(): # If data are valid (correct type, size, etc.)
                
                #Save smeller data:
                smeller = formSmeller.save() # Save in DB
                request.session['idSmeller'] = smeller.id
                
                #Generate game samples to analyze:
                l_allSampleId = getAllId( Sample.objects.all() )
                nbSamplesToAnalyze = 6
                request.session['SampleIdToAnalyze'] = random.sample(l_allSampleId,  nbSamplesToAnalyze) #init
                
                
                #Preparation of the first analyze:
                firstToAnalyze = request.session['SampleIdToAnalyze'][0]   
                firstSample = Sample.objects.get(id=firstToAnalyze)
                firstGuess = Guess(smeller=smeller,sample=firstSample)#Initialize a guess entry for this first sample
                firstGuess.save()
                request.session['guessStep'] = 1
                request.session['currentIdGuess'] = firstGuess.id
                
                #Parameters to generate the first page of game:
                paramToGenerateTemplate['guessStep'] = request.session['guessStep']
                paramToGenerateTemplate['nameSample'] = firstSample.name
                paramToGenerateTemplate['currentSamples'] = getAllName(request.session['SampleIdToAnalyze'], Sample.objects)
            
            else:
                error = 'Invalid format of registration...'
        
        else :
        #### OTHER CONNECTIONS: ###
        #Take the current data:
            currentGuess = Guess.objects.get(id=request.session['currentIdGuess'])
            
            #Save and generation of the different page of the game:
            if 'firstStep' in request.POST.keys() :
                request.session['guessStep'] = 2

            if 'intensity' in request.POST.keys() :
                currentGuess.intensity = request.POST['intensity']
                request.session['guessStep'] = 3
                
            elif 'humor' in request.POST.keys() :
                currentGuess.humor = Humor.objects.get(id=request.POST['humor'])
                request.session['guessStep'] = 4
                
            elif 'note' in request.POST.keys() : 
                currentGuess.note = Note.objects.get(id=request.POST['note'])
                request.session['guessStep'] = 5
                
            elif 'image' in request.POST.keys() : 
                currentGuess.image = Image.objects.language().get(id=request.POST['image'])
                request.session['guessStep'] = 6
                
            elif 'feeling' in request.POST.keys() :
                currentGuess.feeling = request.POST['feeling']
                request.session['guessStep'] = 7
                
            elif 'name' in request.POST.keys() : 
                currentGuess.name = request.POST['name']
                request.session['guessStep'] = 8
                
            currentGuess.save()
    
    else: # if it's not post, it's not safe
        error = 'You try to connect to this game with the wrong way, please, go back to home...'
    
    
    currentGuess = Guess.objects.get(id=request.session['currentIdGuess'])
    
    # Parameters to generate template
    paramToGenerateTemplate['currentSamples'] = getAllName(request.session['SampleIdToAnalyze'], Sample.objects)
    paramToGenerateTemplate['nameSample'] = Sample.objects.get(id=currentGuess.sample_id).name
    
    paramToGenerateTemplate['intensity'] = currentGuess.intensity
    paramToGenerateTemplate['humor'] = currentGuess.humor
    paramToGenerateTemplate['note'] = currentGuess.note
    paramToGenerateTemplate['image'] = currentGuess.image
    paramToGenerateTemplate['feeling'] = currentGuess.feeling
    
    paramToGenerateTemplate['listHumors'] = Humor.objects.all()
    paramToGenerateTemplate['listNotes'] = Note.objects.all()
    paramToGenerateTemplate['listImages'] = Image.objects.all()

    #Preparing next step:
    paramToGenerateTemplate['guessStep'] = request.session['guessStep']
    
    return render(request, 'SmellGuessTemplate/game.html', paramToGenerateTemplate)



def resultView(request):
    """Called view by the URL /result.

    Call calculations to find the mean values of others smellers.
    This view is called by the last page game of a test.

    Parameters
    ----------
    request : HttpRequest object
        Contain many info (GET/POST method, forms data, session data, ...).

    Returns
    -------
    render() : HttpResponse object
        The render() function contain 3 parameters:
            1) Initial request
            2) Path of a template
            3) A dictionary which contains all data accessible in the template (before generation) 
        This function generates an HTML file after analyzing the correct template.

    Examples
    --------

    See also
    --------

    Notes
    -----
    TODO: Secure when refresh/precedent action is used
    TODO: See to improve the save of guess &co (not at each page, but only at the end for instance)

    """
    
    if request.method == 'POST':  # If it's a POST request
        guess = Guess.objects.get(id=request.session['currentIdGuess'])
        guess.name = request.POST['name']
        guess.save()
        
        request.session['guessStep'] = 1      
        
        #In waiting to display images of other results:
        idOfAnalyzedSample = guess.sample_id
        idemGuess = Guess.objects.filter(sample_id=idOfAnalyzedSample).exclude(smeller_id=guess.smeller_id) #Give a list of all guess with same current sample
        intensities = list()
        humors = list()
        notes = list()
        images = list()
        feelings = list()
        names = list()
        for g in idemGuess:
            intensities.append(g.intensity)
            humors.append(g.humor_id)
            notes.append(g.note_id)
            images.append(g.image_id)
            feelings.append(g.feeling)
            names.append(g.name)
    
    else: # if it's not post, it's not safe
        error = 'You try to connect to this game with the wrong way, please, go back to home...'
    
    
    guess = Guess.objects.get(id=request.session['currentIdGuess'])
    smeller = Smeller.objects.get(id=request.session['idSmeller'])
    
    
    paramToGenerateTemplate = dict()
    
    
    #######################################################################"
    #all param to generate:
    paramToGenerateTemplate['intensity'] = guess.intensity
    paramToGenerateTemplate['intensityDisplay'] = 30*guess.intensity/100+40
    paramToGenerateTemplate['humorColor'] = guess.humor.color
    paramToGenerateTemplate['humourColorName'] = (Humor.objects.get(id=guess.humor_id)).name
    paramToGenerateTemplate['noteColor'] = guess.note.color
    paramToGenerateTemplate['noteColorName'] = (Note.objects.get(id=guess.note_id)).name
    paramToGenerateTemplate['pathImage'] = guess.image.pathImage
    paramToGenerateTemplate['imageName'] = (Image.objects.get(id=guess.image_id)).name
    paramToGenerateTemplate['opacityLevelPercent'] = str(guess.feeling*50/100) 
    paramToGenerateTemplate['opacityLevel'] = str(guess.feeling*0.5/100)
    paramToGenerateTemplate['feelingLevel'] = guess.feeling
    paramToGenerateTemplate['name'] = guess.name
    
    
    if len(intensities) == 0 :
	    paramToGenerateTemplate['intensityMean'] = None
	    paramToGenerateTemplate['intensityMeanDisplay'] = None
    else :
	    intensityMean = mean(intensities)
	    paramToGenerateTemplate['intensityMean'] = intensityMean
	    paramToGenerateTemplate['intensityMeanDisplay'] = 30*intensityMean/100+40
	    
    if len(feelings) == 0 :
	    paramToGenerateTemplate['feelingLevelMean'] = None
	    paramToGenerateTemplate['opacityMeanLevelPercent'] = None
	    paramToGenerateTemplate['opacityMeanLevel'] = None
    else :
	    feelingLevelMean = mean(feelings)
	    paramToGenerateTemplate['feelingLevelMean'] = feelingLevelMean
	    paramToGenerateTemplate['opacityLevelMeanPercent'] = str(feelingLevelMean*50/100) 
	    paramToGenerateTemplate['opacityLevelMean'] = str(feelingLevelMean*0.5/100)
    
    maxHumorsId = maxi(humors)
    if isinstance(maxHumorsId, int):#existe et donc non None
        maxHumors = Humor.objects.get(id=maxHumorsId)
        paramToGenerateTemplate['humorColorMean'] = maxHumors.color
        paramToGenerateTemplate['humourColorMeanName'] = (Humor.objects.get(id=maxHumorsId)).name
    else:
        paramToGenerateTemplate['humorColorMean'] = None
        paramToGenerateTemplate['humourColorMeanName'] = _(u"Non disponible")
    
    
    maxNotesId = maxi(notes)
    if isinstance(maxNotesId, int):#existe et donc non None
        maxNotes = Note.objects.get(id=maxNotesId)
        paramToGenerateTemplate['noteColorMean'] = maxNotes.color
        paramToGenerateTemplate['noteColorMeanName'] = (Note.objects.get(id=maxNotesId)).name
    else:
        paramToGenerateTemplate['noteColorMean'] = None
        paramToGenerateTemplate['noteColorMeanName'] = _(u"Non disponible")
        
    maxImagesId = maxi(images)
    if isinstance(maxImagesId, int):#existe et donc non None    
        maxImages = Image.objects.get(id=maxImagesId)
        paramToGenerateTemplate['pathImageMean'] = maxImages.pathImage
        paramToGenerateTemplate['imageMeanName'] = (Image.objects.get(id=maxImagesId)).name
    else:
        paramToGenerateTemplate['pathImageMean'] = None
        paramToGenerateTemplate['imageMeanName'] = _(u"Non disponible")
    
    paramToGenerateTemplate['nameSample'] = Sample.objects.get(id=guess.sample_id).name
    
    
    #######################################################################"
    
    
    paramToGenerateTemplate['guess'] = guess
    paramToGenerateTemplate['listGuess'] = Guess.objects.filter(smeller=smeller);
    
    
    request.session['SampleIdToAnalyze'].remove(guess.sample_id) #Warning: remove method don't return the list minus the element...
    
    paramToGenerateTemplate['remainSamplesToAnalyze'] = []
    for idSample in request.session['SampleIdToAnalyze'] :
	    paramToGenerateTemplate['remainSamplesToAnalyze'].append(Sample.objects.get(id=idSample).name)
    
    
    paramToGenerateTemplate['nbRemainSamplesToAnalyze'] = len(request.session['SampleIdToAnalyze'])
    if paramToGenerateTemplate['nbRemainSamplesToAnalyze'] > 0: #if it remains sample(s) to analyze: 

        sample = Sample.objects.get(id=request.session['SampleIdToAnalyze'][0])
        paramToGenerateTemplate['nameNextSample'] = sample.name
        guess = Guess(smeller=smeller,sample=sample)
        guess.save()
        request.session['currentIdGuess'] = guess.id
    
    #else : DB_to_csv()
    
    return render(request, 'SmellGuessTemplate/result.html', paramToGenerateTemplate)




def errorview(request):
    """Called view by the URL /error.

    Better than a Django error!

    Parameters
    ----------
    request : HttpRequest object
        Contain many info (GET/POST method, forms data, session data, ...).

    Returns
    -------
    render() : HttpResponse object
        The render() function contain 3 parameters:
            1) Initial request
            2) Path of a template
            3) A dictionary which contains all data accessible in the template (before generation) 
        This function generates an HTML file after analyzing the correct template.

    Examples
    --------

    See also
    --------

    Notes
    -----
    
    TODO: See redirection rather render.

    """
    
    #return a page indicating an error has occured
    return render(request, 'SmellGuessTemplate/error.html')


###############################################################
####################    LOCAL FUNCTIONS    ####################
###############################################################
def mean(param):
    
    result = 0
    nb = 0
    
    for val in param:
        if isinstance(val, int):
            nb += 1
            result += val
    if nb > 0:
        result = result / nb
    else:
        result = None  

    #mean in % in fact
    return result



def maxi(param):
    
    from collections import defaultdict
    
    calDict = defaultdict(lambda: 0)
    nb = 0
    
    for val in param:
        if isinstance(val, int):
            nb += 1
            calDict[str(val)] += 1
    
    resultId = 0
    if nb > 0:
        maxCalDict = max(calDict.values())
        for idKey in calDict.keys():
            if calDict[idKey] == maxCalDict:
                resultId = int(idKey)
                
    else:
        resultId = None
    
    return resultId


def DB_to_csv():
    listSmeller = Smeller.objects.all()
    listGuess = Guess.objects.all()
    
    date = time.strftime("%Y-%m-%d_%Hh%Mm%Ss")
    
    sm = open ('Backup/Smeller_'+date+'.csv', 'w+')
    gu = open ('Backup/Guess_'+date+'.csv', 'w+')
    
    sm_header="id;sex;age;date_registration"
    gu_header="id;smeller;sample;intensity;humor;note;image;feeling;name"
    sm.write(sm_header)
    gu.write(gu_header)
    
    
    for s in listSmeller :
        tmp_sentence = "\n"+str(s.id)+";"
        if s.sex != None : tmp_sentence += s.sex+";"
        else : tmp_sentence += ";"
        if s.age != None : tmp_sentence += str(s.age)+";"
        else : tmp_sentence += ";"
        if s.date_registration != None : tmp_sentence += str(s.date_registration)
        sm.write(str(tmp_sentence))
    sm.close()
    
    for g in listGuess :
	tmp_sentence = "\n"+str(g.id)+";"
	if g.smeller != None : tmp_sentence += str(g.smeller.id)+";"
	else : tmp_sentence += ";"
	if g.sample != None : tmp_sentence += g.sample.name+";"
	else : tmp_sentence += ";"
	if g.intensity != None : tmp_sentence += str(g.intensity)+";"
	else : tmp_sentence += ";"
	if g.humor != None : tmp_sentence += g.humor.name+";"
	else : tmp_sentence += ";"
	if g.note != None : tmp_sentence += g.note.name+";"
	else : tmp_sentence += ";"
	if g.image != None : tmp_sentence += g.image.name+";"
	else : tmp_sentence += ";"
	if g.feeling != None : tmp_sentence += str(g.feeling)+";"
	else : tmp_sentence += ";"
	if g.name != None : tmp_sentence += g.name.encode("utf-8")
	gu.write(tmp_sentence)
    gu.close()


def sendZipfileBackup(request) :
    temp = tempfile.TemporaryFile()
    archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
    for nameFile in os.listdir('Backup') :
        if nameFile[0:7] == "Smeller" :
            archive.write('Backup/'+nameFile, 'Smeller/'+nameFile)
        elif nameFile[0:5] == "Guess" :
            archive.write('Backup/'+nameFile, 'Guess/'+nameFile)
        archive.close()
    
    wrapper = FileWrapper(temp)
    response = HttpResponse(wrapper, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=smellerBackup.zip'
    response['Content-Length'] = temp.tell()
    archive.close()
    temp.seek(0)
    return response

        









def demoView(request):
    
    paramToGenerateTemplate = dict()
    
    #First connection:
    if request.session['guessStep'] == None:
        
        request.session['intensity'] = None
        request.session['humorName'] = None
        request.session['humorColor'] = None
        request.session['noteName'] = None
        request.session['noteColor'] = None
        request.session['imageName'] = None
        request.session['imagePathImage'] = None
        request.session['feeling'] = None
        request.session['name'] = None
        
        #Generate game samples to analyze:
        l_allSampleId = getAllId( Sample.objects.all() )
        nbSamplesToAnalyze = 6
        request.session['SampleIdToAnalyze'] = random.sample(l_allSampleId,  nbSamplesToAnalyze) #init
        
        #Preparation of the first analyze:
        firstToAnalyze = request.session['SampleIdToAnalyze'][0]
        request.session['sampleId'] = firstToAnalyze   
        firstSample = Sample.objects.get(id=firstToAnalyze)
        
        #Parameters to generate the first page of game:
        paramToGenerateTemplate['guessStep'] = request.session['guessStep']
        paramToGenerateTemplate['nameSample'] = firstSample.name
        paramToGenerateTemplate['currentSamples'] = getAllName(request.session['SampleIdToAnalyze'], Sample.objects)
        
        request.session['guessStep'] = 1
    
    #Other connections:
    else:       
        #Generation of the different page of the game:
        if 'firstStep' in request.POST.keys() :
            request.session['guessStep'] = 2

        if 'intensity' in request.POST.keys() :
            request.session['intensity'] = request.POST['intensity']
            request.session['guessStep'] = 3
            
        elif 'humor' in request.POST.keys() :
            request.session['humorName'] = Humor.objects.get(id=request.POST['humor']).name
            request.session['humorColor'] = Humor.objects.get(id=request.POST['humor']).color
            request.session['guessStep'] = 4
            
        elif 'note' in request.POST.keys() : 
            request.session['noteName'] = Note.objects.get(id=request.POST['note']).name
            request.session['noteColor'] = Note.objects.get(id=request.POST['note']).color
            request.session['guessStep'] = 5
            
        elif 'image' in request.POST.keys() : 
            request.session['imageName'] = Image.objects.language().get(id=request.POST['image']).name
            request.session['imagePathImage'] = Image.objects.language().get(id=request.POST['image']).pathImage
            request.session['guessStep'] = 6
            
        elif 'feeling' in request.POST.keys() :
            request.session['feeling'] = request.POST['feeling']
            request.session['guessStep'] = 7
            
        elif 'name' in request.POST.keys() : 
            request.session['name'] = request.POST['name']
            request.session['guessStep'] = 8
            
    
    # Parameters to generate template
    paramToGenerateTemplate['currentSamples'] = getAllName(request.session['SampleIdToAnalyze'], Sample.objects)    
    paramToGenerateTemplate['nameSample'] = Sample.objects.get(id=request.session['sampleId']).name
    request.session['nameSample'] = paramToGenerateTemplate['nameSample']
    paramToGenerateTemplate['listHumors'] = Humor.objects.all()
    paramToGenerateTemplate['listNotes'] = Note.objects.all()
    paramToGenerateTemplate['listImages'] = Image.objects.all()

    #Preparing next step:
    paramToGenerateTemplate['guessStep'] = request.session['guessStep']
    
    paramToGenerateTemplate['intensity'] = request.session['intensity']
    paramToGenerateTemplate['humorName'] = request.session['humorName']
    paramToGenerateTemplate['humorColor'] = request.session['humorColor']
    paramToGenerateTemplate['noteName'] = request.session['noteName']
    paramToGenerateTemplate['noteColor'] = request.session['noteColor']
    paramToGenerateTemplate['imageName'] = request.session['imageName']
    paramToGenerateTemplate['imagePathImage'] = request.session['imagePathImage']
    paramToGenerateTemplate['feeling'] = request.session['feeling']
    paramToGenerateTemplate['name'] = request.session['name']
    
    return render(request, 'SmellGuessTemplate/demo.html', paramToGenerateTemplate)







def resultDemoView(request):
    
    if request.method == 'POST':  # If it's a POST request
        
        request.session['guessStep'] = 1      
        
        #In waiting to display images of other results:
        idOfAnalyzedSample = request.session['sampleId']
        idemGuess = Guess.objects.filter(sample_id=idOfAnalyzedSample)
        intensities = list()
        humors = list()
        notes = list()
        images = list()
        feelings = list()
        names = list()
        for g in idemGuess:
            intensities.append(g.intensity)
            humors.append(g.humor_id)
            notes.append(g.note_id)
            images.append(g.image_id)
            feelings.append(g.feeling)
            names.append(g.name)
    
    else: # if it's not post, it's not safe
        error = 'You try to connect to this game with the wrong way, please, go back to home...'
    
    paramToGenerateTemplate = dict()
    
    #all param to generate:
    paramToGenerateTemplate['intensity'] = request.session['intensity']
    paramToGenerateTemplate['intensityDisplay'] = 30 * (int(request.session['intensity']))/100 + 40
    paramToGenerateTemplate['humorColor'] = request.session['humorColor']
    paramToGenerateTemplate['humourColorName'] = request.session['humorName']
    paramToGenerateTemplate['noteColor'] = request.session['noteColor']
    paramToGenerateTemplate['noteColorName'] = request.session['noteName']
    paramToGenerateTemplate['pathImage'] = request.session['imagePathImage']
    paramToGenerateTemplate['imageName'] = request.session['imageName']
    paramToGenerateTemplate['opacityLevelPercent'] = str((int(request.session['feeling']))*50/100) 
    paramToGenerateTemplate['opacityLevel'] = str((int(request.session['feeling']))*0.5/100)
    paramToGenerateTemplate['feelingLevel'] = request.session['feeling']
    paramToGenerateTemplate['name'] = request.session['name']
    
    
    if len(intensities) == 0 :
        paramToGenerateTemplate['intensityMean'] = None
        paramToGenerateTemplate['intensityMeanDisplay'] = None
    else :
        intensityMean = mean(intensities)
        paramToGenerateTemplate['intensityMean'] = intensityMean
        paramToGenerateTemplate['intensityMeanDisplay'] = 30*intensityMean/100+40
        
    if len(feelings) == 0 :
        paramToGenerateTemplate['feelingLevelMean'] = None
        paramToGenerateTemplate['opacityMeanLevelPercent'] = None
        paramToGenerateTemplate['opacityMeanLevel'] = None
    else :
        feelingLevelMean = mean(feelings)
        paramToGenerateTemplate['feelingLevelMean'] = feelingLevelMean
        paramToGenerateTemplate['opacityLevelMeanPercent'] = str(feelingLevelMean*50/100) 
        paramToGenerateTemplate['opacityLevelMean'] = str(feelingLevelMean*0.5/100)
    
    maxHumorsId = maxi(humors)
    if isinstance(maxHumorsId, int):#existe et donc non None
        maxHumors = Humor.objects.get(id=maxHumorsId)
        paramToGenerateTemplate['humorColorMean'] = maxHumors.color
        paramToGenerateTemplate['humourColorMeanName'] = (Humor.objects.get(id=maxHumorsId)).name
    else:
        paramToGenerateTemplate['humorColorMean'] = None
        paramToGenerateTemplate['humourColorMeanName'] = _(u"Non disponible")
    
    
    maxNotesId = maxi(notes)
    if isinstance(maxNotesId, int):#existe et donc non None
        maxNotes = Note.objects.get(id=maxNotesId)
        paramToGenerateTemplate['noteColorMean'] = maxNotes.color
        paramToGenerateTemplate['noteColorMeanName'] = (Note.objects.get(id=maxNotesId)).name
    else:
        paramToGenerateTemplate['noteColorMean'] = None
        paramToGenerateTemplate['noteColorMeanName'] = _(u"Non disponible")
        
    maxImagesId = maxi(images)
    if isinstance(maxImagesId, int):#existe et donc non None    
        maxImages = Image.objects.get(id=maxImagesId)
        paramToGenerateTemplate['pathImageMean'] = maxImages.pathImage
        paramToGenerateTemplate['imageMeanName'] = (Image.objects.get(id=maxImagesId)).name
    else:
        paramToGenerateTemplate['pathImageMean'] = None
        paramToGenerateTemplate['imageMeanName'] = _(u"Non disponible")
    
    paramToGenerateTemplate['nameSample'] = request.session['nameSample']
    
    
    #######################################################################"
    
    request.session['SampleIdToAnalyze'].remove(request.session['sampleId']) #Warning: remove method don't return the list minus the element...
    
    paramToGenerateTemplate['remainSamplesToAnalyze'] = []
    for idSample in request.session['SampleIdToAnalyze'] :
        paramToGenerateTemplate['remainSamplesToAnalyze'].append(Sample.objects.get(id=idSample).name)
    
    
    paramToGenerateTemplate['nbRemainSamplesToAnalyze'] = len(request.session['SampleIdToAnalyze'])
    if paramToGenerateTemplate['nbRemainSamplesToAnalyze'] > 0: #if it remains sample(s) to analyze: 
        request.session['sampleId'] = request.session['SampleIdToAnalyze'][0]
        sample = Sample.objects.get(id=request.session['sampleId'])
        paramToGenerateTemplate['nameNextSample'] = sample.name
    else:
        request.session['sampleId'] = None
    
    #RE-initialization of session variable:
    request.session['intensity'] = None
    request.session['humorName'] = None
    request.session['humorColor'] = None
    request.session['noteName'] = None
    request.session['noteColor'] = None
    request.session['imageName'] = None
    request.session['imagePathImage'] = None
    request.session['feeling'] = None
    request.session['name'] = None

    return render(request, 'SmellGuessTemplate/demoResult.html', paramToGenerateTemplate)




###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
'''
# Modele de fonction de la vue :
def fonctionAppeleeParURL(request, autresVar):
    return render(request, 'templateAppelePourgeneration', dict={'varName': valeur})

# Modele d'une variable de session (cad variable qui reste accessible tant que le navigateur n'est pas ferme ou que la var soit supprimÃ©e)
request.session['KeyName']
'''


if __name__=="__main__": 
    
    print 'Test in local\n.'

    
    