#-*- coding: utf-8 -*-

"""
Authors : 
- Florian Thonier, florian.thonier@gmail.com (2014)
"""


################################################################
#######################    LIBRARIES    ########################
################################################################
# Django libs:
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from django.core.servers.basehttp import FileWrapper
from django.utils.encoding import smart_str, smart_unicode 

# External libs:
from datetime import datetime
import random
import time
import codecs
import os, tempfile, zipfile
from base64 import decodestring

from django.db import models
from SmellGuess.models  import *
from SmellGalaxy.models import *
from SmellGift.models   import *

################################################################
#########################    VIEWS    ##########################
################################################################


# Nathan view
def graphesView(request):
    paramToGenerateTemplate = dict()

    paramToGenerateTemplate['guess']             = Guess.objects.all()
    paramToGenerateTemplate['sample']            = Sample.objects.all()
	#Delete old data
    GraphHistogramme.objects.all().delete()
    GraphPie.objects.all().delete()
    GraphLines.objects.all().delete()
    #Get news data
    paramToGenerateTemplate['HistoGraphs']  = createListHisto()
    paramToGenerateTemplate['PiesGraphs']   = createListPie()
    paramToGenerateTemplate['LinesGraphs']  = createListLines()

    return render(request, 'SmellGalaxyTemplate/Graphes.html', paramToGenerateTemplate) 
    
def createListHisto():
	#GraphHistogramme(title="", button="", orderedName="", abscisseName="", data=getdata...(), dataError =getdata...())
	if not GraphHistogramme.objects.filter(title="Intensity & Feeling by sex"): 
		GraphHistogramme(title="Intensity & Feeling by sex", button="Data by sex", orderedName="Intensity & feeling", abscisseName="sex of giver", data= getDataBySex(), dataError = "").save()
	if not GraphHistogramme.objects.filter(title="Intensity & Feeling by age"): 
		GraphHistogramme(title="Intensity & Feeling by age", button="Data by age", orderedName="Intensity & feeling", abscisseName="categories of age", data= getDataBySliceOfAge(), dataError = "").save()
	if not GraphHistogramme.objects.filter(title="Intensity & Feeling by use of deodorant"): 
		GraphHistogramme(title="Intensity & Feeling by use of deodorant", button="Data by use of deodorant", orderedName="Intensity & feeling", abscisseName="use of deodorant of giver", data= getDataByDeo(), dataError = "").save()
	toReturn = GraphHistogramme.objects.all()
	return toReturn


def createListPie():
	#GraphPie(title="", button="", description="", data=getdata...())
	if not GraphPie.objects.filter(title="Repartition by sex"): 	
		GraphPie(title="Repartition by sex",               button="Pie by sex",     description="Repartition by sex", data=pieByCritereSex).save()
	if not GraphPie.objects.filter(title="Repartition between slice of Age"): 	
		GraphPie(title="Repartition between slice of Age", button="Pie by age",     description="Repartition between slice of Age", data=pieByCritereSliceOfAge()).save()
	if not GraphPie.objects.filter(title="Repartition by smoker"): 	
		GraphPie(title="Repartition by smoker",            button="Pie by smoking", description="Repartition by smoker", data=pieByCritereSmoker()).save()
	toReturn = GraphPie.objects.all()
	return toReturn

def createListLines():
	#GraphLines(title="", button="", abscisseName="", orderedName="", nameLine1="",dataLine1=getdata...(), nameLine2="", dataLine2 =getdata...())
	if not GraphLines.objects.filter(title="Pleasanteness in function of intensity"): 	
		GraphLines(title="Pleasanteness in function of intensity", button="pleasanteness by intensity", abscisseName="Intensity", orderedName="Feeling", nameLine1="raw data", dataLine1=intensityByFeeling(), nameLine2="Center data", dataLine2 =intensityByFeelingCenter(), subtitle="").save()
	toReturn = GraphLines.objects.all()
	return toReturn
