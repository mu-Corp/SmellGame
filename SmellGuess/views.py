#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################
# Django libs:
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render 

# External libs:
from datetime import datetime

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
                smeller = formSmeller.save() # Save in DB
                sample = Sample.objects.get(id=1) # A tirer au sort
                guess = Guess(smeller=smeller,sample=sample)
                guess.save()
                
                # Full sessions variables
                request.session['idSmeller'] = smeller.id
                request.session['nameSmeller'] = smeller.name
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
    paramToGenerateTemplate['intensity'] = guess.intensity
    paramToGenerateTemplate['humor'] = guess.humor
    paramToGenerateTemplate['note'] = guess.note
    paramToGenerateTemplate['image'] = guess.image
    paramToGenerateTemplate['feeling'] = guess.feeling

	
    return render(request, 'SmellGuessTemplate/game.html', paramToGenerateTemplate)

def errorview(request):
    #return a page indicating an error has occured
    return render(request, 'SmellGuessTemplate/error.html')

###############################################################
####################    LOCAL FUNCTIONS    ####################
###############################################################

def save_GuessModelForm(guessModelForm, sample, smeller):
    guess = Guess() # Init Guess
    
    # Update attr
    guess.intensity = guessModelForm.data['intensity']
    guess.odor = guessModelForm.data['odor']
    guess.sample = sample
    guess.smeller = smeller
    
    # Save guess
    guess.save()
        
    # Add parfumes
    listIdPerfumes = guessModelForm.data['perfumes'][:-1].split(';')
    for idPerfume in listIdPerfumes :
        perfume = Perfume.objects.get(id=idPerfume)
        guess.perfumes.add(perfume)
    
    # Save guess with parfumes
    guess.save()
    
    return guess

###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__=="__main__": 
    
    print 'Test in local\n.'
    
    