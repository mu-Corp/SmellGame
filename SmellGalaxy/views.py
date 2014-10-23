#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def DemoGraphes(request):
	"""
	A simple view for a simple demonstration
	"""
	return render(request, 'SmellGalaxyTemplate/Graphes.html')