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
    return render(request, 'SmellGuessTemplate/game.html', {'current_date': datetime.now()})
    '''
    #user==True si le smeller s'est bien identifié auparavant sur la page d'identification
    if user == 1:
        return render(request, 'SmellGuessTemplate/game.html', {'current_date': datetime.now()})
    else:
        return render(request, 'SmellGuessTemplate/identification.html', {'current_date': datetime.now()})
    '''

###############################################################
####################    LOCAL FUNCTIONS    ####################
###############################################################


###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__=="__main__": 
    
    print 'Test in local\n.'
    
    