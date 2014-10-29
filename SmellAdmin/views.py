#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################
# Django libs:
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout


# Local import:
from SmellGuess.models import Sample
from forms import ConnexionForm

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
	paramToGenerateTemplate['error'] = False
	#Select all data in DB:
	paramToGenerateTemplate['l_allSamples'] = Sample.objects.all()
	
	
	if request.method == 'POST':	
	
		form = ConnexionForm(request.POST)
		paramToGenerateTemplate['form'] = ConnexionForm()
		
		if form.is_valid():

			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
			
			if user:  # Si l'objet renvoyé n'est pas None
				login(request, user)  # nous connectons l'utilisateur
				
				request.session['demoMode'] = False #If admin co, disable the mode demo
				
			else: # sinon une erreur sera affichée
				paramToGenerateTemplate['error'] = True

	else:#Connection before identification
		paramToGenerateTemplate['form'] = ConnexionForm()

	
	return render(request, 'SmellAdminTemplate/main.html', paramToGenerateTemplate)






def adminThankView(request):
	
	if request.method == 'POST':	

		for sample in Sample.objects.all() :
			if str(sample.name) in request.POST :
				sample.available = True
			else:
				sample.available = False
				
			sample.save()
			
	return render(request, 'SmellAdminTemplate/thanks.html')	
	





def decoView(request):
	
	logout(request)
	
	request.session['demoMode'] = True #If admin deco, active the mode demo
			
	return render(request, 'SmellAdminTemplate/deco.html')	
	


