#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################
# Django libs:
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render

'''
# Local import:
#from forms import SampleGiverForm
from SmellGift.models import SampleGiver, Food
from SmellGuess.models import Sample
'''
################################################################
#########################    VIEWS    ##########################
################################################################

def adminView(request):

	form = None

	return render(request, 'SmellAdminTemplate/main.html', {'form': form})

