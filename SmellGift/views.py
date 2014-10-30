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
from SmellGuess.models import Sample

################################################################
#########################    VIEWS    ##########################
################################################################

def giftView(request):
	form = SampleGiverForm()
	form.fields["foodRecentlyEaten"].queryset = Food.objects.all()
	
	return render(request, 'SmellGiftTemplate/gift.html', {'form': form})




def getAllSampleName():
	result = list()
	for sample in Sample.objects.all():
		result.append(sample.name)
	return result
		

def thanksView(request) :
	
	paramToGenerateTemplate = dict()
	paramToGenerateTemplate['nameSample'] = 'demo'
	
	if 'demoMode' not in request.session.keys():
		request.session['demoMode'] = True
	
	if request.session['demoMode'] == False:
		if request.method == 'POST':
			formGiver = SampleGiverForm(request.POST)
			if formGiver.is_valid() :
				giver = formGiver.save()
				sample = Sample(sampleGiver=giver)
				sample.save()
				
				#Generate a correct sample name:
				l_sampleName = getAllSampleName()
				sessionName = 'B'
				i = 1
				sampleName = sessionName + str(i)
				while sampleName in l_sampleName:
					i += 1
					sampleName = sessionName + str(i)
				
				sample.name = sampleName
				sample.save()
				
				paramToGenerateTemplate['nameSample'] = sampleName
				
	
	paramToGenerateTemplate['demoMode'] = request.session['demoMode']
	
	return render(request, 'SmellGiftTemplate/thanks.html', paramToGenerateTemplate)








