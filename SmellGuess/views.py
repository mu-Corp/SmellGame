#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render

from datetime import datetime

################################################################
#######################    FUNCTIONS    ########################
################################################################


def home(request):    
    return render(request, 'SmellGuessTemplate/home.html', {'current_date': datetime.now()})


def enter(request):
    return render(request, 'SmellGuessTemplate/identification.html', {'current_date': datetime.now()})


#######################




#######################


def game(request):
    
    return render(request, 'SmellGuessTemplate/game.html', {'current_date': datetime.now()})


###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__=="__main__": 
    
    print 'Test in local\n.'
    
    