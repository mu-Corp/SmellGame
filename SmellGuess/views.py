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
# Modèle de fonction de la vue :
def fonctionAppeleeParURL(request, autresVar):
    return render(request, 'templateAppelePourgeneration', dict={'varName': valeur})

# Modèle d'une variable de session (cad variable qui reste accessible tant que le navigateur n'est pas fermé ou que la var soit supprimée)
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
    return render(request, 'SmellGuessTemplate/home.html', {'current_date': datetime.now()})
    
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
                
                #Random id of samples to analyze:
                allSampleIds = range(1, 51)#list contains 1, 2, ..., 50
                nbSamplesToAnalyze = 6
                request.session['currentSamples'] = random.sample(allSampleIds,  nbSamplesToAnalyze)
                firstToAnalyze = 1#request.session['currentSamples'][0]
                
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
                
            else:
                error = 'invalid data...'
        
        else : # Else Sample is guessed
            
            guess = Guess.objects.get(id=request.session['idGuess'])
            
            if request.session['guessStep']   == 2 : guess.intensity = request.POST['intensity']
            elif request.session['guessStep'] == 3 : guess.humor = Humor.objects.get(id=request.POST['humor'])
            elif request.session['guessStep'] == 4 : guess.note = Note.objects.get(id=request.POST['note'])
            elif request.session['guessStep'] == 5 : guess.image = Image.objects.get(id=request.POST['image'])
            elif request.session['guessStep'] == 6 : guess.feeling = request.POST['feeling']
            elif request.session['guessStep'] == 7 : guess.name = request.POST['name']
            
            guess.save()
            
            request.session['guessStep'] += 1 # Update step
        
    else: # if it's not post, it's not safe
        error = 'You try to connect to this game with the wrong way, please, go back to home...'
    
    guess = Guess.objects.get(id=request.session['idGuess'])
    
    paramToGenerateTemplate = dict()
    paramToGenerateTemplate['listHumors'] = Humor.objects.all()
    paramToGenerateTemplate['listNotes'] = Note.objects.all()
    paramToGenerateTemplate['listImages'] = Image.objects.all()
    
    paramToGenerateTemplate['guessStep'] = request.session['guessStep']
    
        
    paramToGenerateTemplate['keepingSamplesToAnalyze'] = "Echantillon tiré (en cours de modif) : " + str(request.session['idGuess'])#request.session['currentSamples'].remove(request.session['idGuess'])
    
    paramToGenerateTemplate['intensity'] = guess.intensity
    paramToGenerateTemplate['humor'] = guess.humor
    paramToGenerateTemplate['note'] = guess.note
    paramToGenerateTemplate['image'] = guess.image
    paramToGenerateTemplate['feeling'] = guess.feeling

    return render(request, 'SmellGuessTemplate/game.html', paramToGenerateTemplate)

def resultView(request):
	if request.method == 'POST':  # If it's a POST request
		guess = Guess.objects.get(id=request.session['idGuess'])
		guess.name = request.POST['name']
		guess.save()
		
		img = open("guessImages/"+str(guess.id)+".png", "ab")
		img.write(decode_base64(request.POST['imageBase64'][22:]))
		img.close()
		
	else: # if it's not post, it's not safe
		error = 'You try to connect to this game with the wrong way, please, go back to home...'
	
	guess = Guess.objects.get(id=request.session['idGuess'])
	smeller = Smeller.objects.get(id=request.session['idSmeller'])
	paramToGenerateTemplate = dict()
	paramToGenerateTemplate['guess'] = guess
	paramToGenerateTemplate['listGuess'] = Guess.objects.filter(smeller=smeller);
	
	return render(request, 'SmellGuessTemplate/result.html', paramToGenerateTemplate)

def errorview(request):
    #return a page indicating an error has occured
    return render(request, 'SmellGuessTemplate/error.html')

###############################################################
####################    LOCAL FUNCTIONS    ####################
###############################################################

<<<<<<< HEAD
def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += b'='* missing_padding
    return decodestring(data)

=======
import codecs
from django.utils.encoding import smart_str, smart_unicode
>>>>>>> 1c5b4933a06124a498117ea8e1742274730f65e0

def SQL_to_csv():
    listSmeller = Smeller.objects.all()
    listGuess = Guess.objects.all()

    sm = open ('Smeller.csv', 'w+')
    gu = open ('Guess.csv', 'w+')
    
    sm_header="id;sex;age;date_registration"
    gu_header="id;smeller;sample;intensity;humor;note;image;feeling;name"
    sm.write(sm_header)
    gu.write(gu_header)
    
    
    for s in listSmeller :
        tmp_sentence="\n"+ str(s.id)+ ";" + s.sex+ ";"+ str(s.age)+ ";"+ str(s.date_registration)
        #tmp_sentence="\n"+ str(s.id)+ ";"+ s.name+ ";"+ s.sex+ ";"+ str(s.age)+ ";"+ str(s.date_registration) #obsolete
        sm.write(str(tmp_sentence))
        #s.sample.id
    sm.close()
    
    for g in listGuess :
        #print ( "\n", g.id, ";", g.id_smeller, ";", g.id_Sample, ";", g.intensity, ";", g.humor, ";", g.note, ";", g.image, ";", g.feeling, ";", g.name )
        tmp_sentence="\n"+ str(g.id) + ";"+ str(g.smeller.id)+ ";"+str(g.sample.id)+";"+str(g.intensity)+";"+str(g.humor.name)+";"+str(g.note.name)+";"+str(g.image.name)+ ";"+ str(g.feeling)+ ";"+ smart_str(g.name)
        gu.write(str(tmp_sentence))
        #g.smeller.id
    gu.close()
   
SQL_to_csv()
#"id;name;sex;age:date_registration"
#"1;Flo;F;18;01/01/14"    
#"id;id_Smeller;id_Sample;intensity;humor;note;image;feeling;name"
#"1;1;1;20;COLERE;FRUITE;AIL;80;MA MERE"



###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__=="__main__": 
    
    print 'Test in local\n.'

    
    