#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################
# Django libs:
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render


# Local import:
from SmellGuess.models import Sample

################################################################
#########################    VIEWS    ##########################
################################################################


def getSampleInfo(l_objects, objectType):
	result = dict()
	
	l_allId = list()   
	for obj in l_objects:
		l_allId.append(obj.id)
	
	for currentId in l_allId:
		result[currentId] = objectType.get(id=currentId).name
	
	return result



def getAllAvailableId(l_objects):
	l_allId = list()   
	
	for obj in l_objects:
		
		if obj.available == 1:
			l_allId.append(obj.id)
	
	return l_allId



def adminView(request):

	paramToGenerateTemplate = dict()

	#Select all data in DB:
	l_allSamples = Sample.objects.all()
	paramToGenerateTemplate['d_allNameSamplesById'] = getSampleInfo(l_allSamples, Sample.objects)
	paramToGenerateTemplate['l_allIdAvailableSamples'] = getAllAvailableId(l_allSamples)


	return render(request, 'SmellAdminTemplate/main.html', paramToGenerateTemplate)



def adminThankView(request):
	
	'''
	if request.method == 'POST':
		
		for sample in Sample.objects.all() :
			
			postValue = request.POST[str(sample.id)]
			
			if postValue == "on":
				sample.available = True
			else:
				sample.available = 0
			
			sample.save()
	'''
	
	
	return render(request, 'SmellAdminTemplate/thanks.html')	
	








