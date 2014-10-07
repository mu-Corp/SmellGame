#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################
# Django libs:
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render

# Local import:
from forms import SampleGiverForm
from SmellGift.models import SampleGiver, Food


################################################################
#########################    VIEWS    ##########################
################################################################

def giftView(request):
	form = SampleGiverForm()
	return render(request, 'SmellGiftTemplate/gift.html', {'form': form})