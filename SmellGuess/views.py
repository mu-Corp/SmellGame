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
from forms import SmellerModelForm, GuessModelForm 
from SmellGuess.models import Smeller, Sample, Guess, Perfume

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
    request.session['index_listSamples'] = None
    
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
    
    listPerfumes = Perfume.objects.all() # Get all perfumes from DB
    listSamples = Sample.objects.all() # Get all samples from DB
    
    # Collect data from smeller from registration form (POST method):
    if request.method == 'POST':  # If it's a POST request
        
        # If Smeller is not registrated = first visit of user on game page (TODO: conserve session var if return to registration page)
        if request.session['idSmeller'] == None : 
            
            formSmeller = SmellerModelForm(request.POST)  # then data is collected.

            if formSmeller.is_valid(): # If data are valid (correct type, size, etc.)
                error = 'no error'
                smeller = formSmeller.save() # Save in DB
                
                # Full sessions variables
                request.session['idSmeller'] = smeller.id
                request.session['nameSmeller'] = smeller.name
                request.session['index_listSamples'] = 0
            
            else:
                error = 'invalid data...'
        
        else : # Else Sample is guessed
            error = 'no error'
            formGuess = GuessModelForm(request.POST) # Guess data is collected
            index_listSamples = request.session['index_listSamples'] # Get index of sample guessed
            # Save guess with data form, sample and smeller
            save_GuessModelForm(formGuess, listSamples[index_listSamples], Smeller.objects.get(id=request.session['idSmeller']))
            request.session['index_listSamples'] += 1 # Update index
        
    else: # if it's not post, it's not safe
        error = 'You try to connect to this game with the wrong way, please, go back to home...'
    
    index_listSamples = request.session['index_listSamples']
    formGuess = GuessModelForm()
    
    # Dict to transfer to the template in render:
    paramToGenerateTemplate = dict()
    
    #Store data in the dicstionnary:
    paramToGenerateTemplate['error'] = error
    paramToGenerateTemplate['smeller'] = Smeller.objects.get(id=request.session['idSmeller'])
    paramToGenerateTemplate['name_sample'] = listSamples[index_listSamples].name
    paramToGenerateTemplate['form'] = formGuess
    paramToGenerateTemplate['listPerfumes'] = listPerfumes
    
    # To finish, generate the template game to send to user:
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
    
    