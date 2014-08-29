#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render

from forms import SmellerModelForm

from datetime import datetime

################################################################
#########################    VIEWS    ##########################
################################################################
'''
Modèle de fonctiond de la vue :
def fonctionAppeleeParURL(request, autresVar):
    return render(request, 'templateAppelePourgeneration', dict={'varName': valeur})
'''

def homeView(request):
    return render(request, 'SmellGuessTemplate/home.html', {'current_date': datetime.now()})

def homeViewTest(request):
    return render(request, 'SmellGuessTemplate/home.html', {'current_date': 2014})
    
#######################

def registrationView(request):
    form = SmellerModelForm()
    return render(request, 'SmellGuessTemplate/registration.html', {'current_date': datetime.now(), 'form': form})

#######################

def gameView(request):
    
    # Dict to transfer to the template in render:
    paramToGenerateTemplate = dict()
    
    paramToGenerateTemplate['idFromPOST']                  = None 
    paramToGenerateTemplate['nameFromPOST']                = None 
    paramToGenerateTemplate['emailFromPOST']               = None 
    paramToGenerateTemplate['sexFromPOST']                 = None 
    paramToGenerateTemplate['ageFromPOST']                 = None 
    paramToGenerateTemplate['samplesFromPOST']             = None 
    
    paramToGenerateTemplate['idFromDB']                  = None 
    paramToGenerateTemplate['nameFromDB']                = None 
    paramToGenerateTemplate['emailFromDB']               = None 
    paramToGenerateTemplate['sexFromDB']                 = None 
    paramToGenerateTemplate['ageFromDB']                 = None 
    paramToGenerateTemplate['date_registrationFromDB']   = None 
    paramToGenerateTemplate['samplesFromDB']             = None 
    
    
    # Collect data from smeller from registration form (POST method):
    if request.method == 'POST':  # If it's a POST request
        form = SmellerModelForm(request.POST)  # then data is collected.

        if form.is_valid(): # If data are valid (correct type, size, etc.)

            error = 'no error'

            # Store specific data in local variable (TO DO: use directly a full object...):
            #paramToGenerateTemplate['idFromPOST']                  = form.cleaned_data['id']
            paramToGenerateTemplate['nameFromPOST']                = form.cleaned_data['name']
            paramToGenerateTemplate['emailFromPOST']               = form.cleaned_data['email']
            paramToGenerateTemplate['sexFromPOST']                 = form.cleaned_data['sex']
            paramToGenerateTemplate['ageFromPOST']                 = form.cleaned_data['age']
            

            # Save date in DB:
            
            
            
            # Load data in DB:
            paramToGenerateTemplate['nameFromDB']                = 'Ho ! Je suis coincé dans la BDD !' 
            paramToGenerateTemplate['emailFromDB']               = None 
            paramToGenerateTemplate['sexFromDB']                 = None 
            paramToGenerateTemplate['ageFromDB']                 = None 
            
        else:
            error = 'invalid data...'

    else: # if it's not post, it's not safe
        error = 'You try to connect to this game with the wrong way, please, go back to home...'
    
    
    #Store data in the dicstionnary:
    paramToGenerateTemplate['error'] = error
    
    
    # To finish, generate the template game to send to user:
    return render(request, 'SmellGuessTemplate/game.html', paramToGenerateTemplate)


###############################################################
####################    LOCAL FUNCTIONS    ####################
###############################################################


###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__=="__main__": 
    
    print 'Test in local\n.'
    
    