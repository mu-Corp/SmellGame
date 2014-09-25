#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################
# Django libs:
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render 

# External libs:
from datetime import datetime
import random
from base64 import decodestring

# Local import:
from forms import SmellerModelForm 
from SmellGuess.models import Smeller, Sample, Guess, Image, Humor, Note

################################################################
#########################    VIEWS    ##########################
################################################################
'''
# ModÃ¨le de fonction de la vue :
def fonctionAppeleeParURL(request, autresVar):
    return render(request, 'templateAppelePourgeneration', dict={'varName': valeur})

# ModÃ¨le d'une variable de session (cad variable qui reste accessible tant que le navigateur n'est pas fermÃ© ou que la var soit supprimÃ©e)
request.session['KeyName']
'''

# Function call when the URL /home/ is call:
def homeView(request):
    
    #TODO: delete all var and delete data from uncomplete game (possible)
    
    # RE-Initialization of variable of session (use during all the session):
    request.session['idSmeller'] = None
    request.session['nameSmeller'] = None
    request.session['idSample'] = None
    request.session['idGuess'] = None
    request.session['guessStep'] = None
    
    # Render:    
    return render(request, 'SmellGuessTemplate/home.html',{})#{'nb': nb, 'intensity': intensity, 'color': color, 'note': note, 'image': image, 'opacity': opacity, 'name': name})
    
#######################
# Function call when the URL /registration/ is call:
def registrationView(request):
    
    form = SmellerModelForm()
    
    return render(request, 'SmellGuessTemplate/registration.html', {'current_date': datetime.now(), 'form': form})

#######################
# Function call when the URL /game/ is call:
# TODO: Use var in URL to generate a specific game page
def gameView(request):
    
    # Collect data from smeller from registration form (POST method):
    if request.method == 'POST':  # If it's a POST request
        
        # If Smeller is not registrated = first visit of user on game page (TODO: conserve session var if return to registration page)
        if request.session['idSmeller'] == None : 
            
            formSmeller = SmellerModelForm(request.POST)  # then data is collected.
            
            if formSmeller.is_valid(): # If data are valid (correct type, size, etc.)
                
                ################################################
                #Random id of samples to analyze:
                allSampleIds = range(1, 51)#list contains 1, 2, ..., 50
                nbSamplesToAnalyze = 6
                request.session['SamplesToAnalyze'] = random.sample(allSampleIds,  nbSamplesToAnalyze) #init
                firstToAnalyze = request.session['SamplesToAnalyze'][0]
                ################################################
                
                
                smeller = formSmeller.save() # Save in DB
                sample = Sample.objects.get(id=firstToAnalyze)
                guess = Guess(smeller=smeller,sample=sample)
                guess.save()
                
                # Full sessions variables
                request.session['idSmeller'] = smeller.id
                #request.session['nameSmeller'] = smeller.name #obsolete
                request.session['idSample'] = sample.id
                request.session['idGuess'] = guess.id
                request.session['guessStep'] = 1
                request.session['remainSamplesToAnalyze'] = nbSamplesToAnalyze #init
                
            else:
                error = 'invalid data...'
        
        else : # Else (Sample-> NON) Smeller is guessed
            
            guess = Guess.objects.get(id=request.session['idGuess'])
            
            if request.session['guessStep']   == 2 : guess.intensity = request.POST['intensity']
            elif request.session['guessStep'] == 3 : guess.humor = Humor.objects.get(id=request.POST['humor'])
            elif request.session['guessStep'] == 4 : guess.note = Note.objects.get(id=request.POST['note'])
            elif request.session['guessStep'] == 5 : guess.image = Image.objects.get(id=request.POST['image'])
            elif request.session['guessStep'] == 6 : guess.feeling = request.POST['feeling']
            elif request.session['guessStep'] == 7 : 
                guess.name = request.POST['name']
                
            guess.save()
            
            request.session['guessStep'] += 1 # Update step
        
        
    else: # if it's not post, it's not safe
        error = 'You try to connect to this game with the wrong way, please, go back to home...'
    
    
    
    #In all cases:
    guess = Guess.objects.get(id=request.session['idGuess'])
    
    
    
    
    paramToGenerateTemplate = dict()
    paramToGenerateTemplate['listHumors'] = Humor.objects.all()
    paramToGenerateTemplate['listNotes'] = Note.objects.all()
    paramToGenerateTemplate['listImages'] = Image.objects.all()
    
    paramToGenerateTemplate['guessStep'] = request.session['guessStep']
    
    
    #Random story!    
    paramToGenerateTemplate['currentSamples'] = request.session['SamplesToAnalyze']
    paramToGenerateTemplate['idSample'] = request.session['idSample']
    
    
    paramToGenerateTemplate['intensity'] = guess.intensity
    paramToGenerateTemplate['humor'] = guess.humor
    paramToGenerateTemplate['note'] = guess.note
    paramToGenerateTemplate['image'] = guess.image
    paramToGenerateTemplate['feeling'] = guess.feeling

    
    
    return render(request, 'SmellGuessTemplate/game.html', paramToGenerateTemplate)








# ...
def resultView(request):
    
    if request.method == 'POST':  # If it's a POST request
        guess = Guess.objects.get(id=request.session['idGuess'])
        guess.name = request.POST['name']
        guess.save()
        
        
        request.session['guessStep'] = 0      
        
        '''
        img = open("guessImages/"+str(guess.id)+".png", "ab")
        img.write(decode_base64(request.POST['imageBase64'][22:]))
        img.close()
        '''
        #In waiting to display images of other results:
        idOfAnalyzedSample = request.session['idSample']
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
    
    
    guess = Guess.objects.get(id=request.session['idGuess'])
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
        paramToGenerateTemplate['humourColorMeanName'] = "Non disponible"
    
    
    maxNotesId = maxi(notes)
    if isinstance(maxNotesId, int):#existe et donc non None
        maxNotes = Note.objects.get(id=maxNotesId)
        paramToGenerateTemplate['noteColorMean'] = maxNotes.color
        paramToGenerateTemplate['noteColorMeanName'] = (Note.objects.get(id=maxNotesId)).name
    else:
        paramToGenerateTemplate['noteColorMean'] = None
        paramToGenerateTemplate['noteColorMeanName'] = "Non disponible"
        
    maxImagesId = maxi(images)
    if isinstance(maxImagesId, int):#existe et donc non None    
        maxImages = Image.objects.get(id=maxImagesId)
        paramToGenerateTemplate['pathImageMean'] = maxImages.pathImage
        paramToGenerateTemplate['imageMeanName'] = (Image.objects.get(id=maxImagesId)).name
    else:
        paramToGenerateTemplate['pathImageMean'] = None
        paramToGenerateTemplate['imageMeanName'] = "Non disponible"
    
    paramToGenerateTemplate['idSample'] = request.session['idSample']
    
    
    #######################################################################"
    
    
    paramToGenerateTemplate['guess'] = guess
    paramToGenerateTemplate['listGuess'] = Guess.objects.filter(smeller=smeller);
    
    
    request.session['SamplesToAnalyze'].remove(request.session['idSample']) #Warning: remove method don't return the list minus the element...
    paramToGenerateTemplate['remainSamplesToAnalyze'] = request.session['SamplesToAnalyze']
    
    
    paramToGenerateTemplate['nbRemainSamplesToAnalyze'] = len(request.session['SamplesToAnalyze'])
    if paramToGenerateTemplate['nbRemainSamplesToAnalyze'] > 0: #if it remains sample(s) to analyze: 

        sample = Sample.objects.get(id=request.session['SamplesToAnalyze'][0])
        request.session['idSample'] = sample.id
	paramToGenerateTemplate['idNextSample'] = sample.id
        guess = Guess(smeller=smeller,sample=sample)
        guess.save()
        request.session['idGuess'] = guess.id
    
    return render(request, 'SmellGuessTemplate/result.html', paramToGenerateTemplate)




# ...
def errorview(request):
    #return a page indicating an error has occured
    return render(request, 'SmellGuessTemplate/error.html')

#[15, 43, 25, 12, 28, 21]
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


###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__=="__main__": 
    
    print 'Test in local\n.'

    
    