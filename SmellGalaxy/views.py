#-*- coding: utf-8 -*-

"""
Authors: 
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
    paramToGenerateTemplate['HistoGraphs']  = createListHisto()
    paramToGenerateTemplate['PiesGraphs']   = createListPie()
    paramToGenerateTemplate['LinesGraphs']  = createListLines()

    return render(request, 'SmellGalaxyTemplate/Graphes.html', paramToGenerateTemplate) 
    
def createListHisto():
	listHisto = []
	# Intensity & Feeling by sex
	listHisto.append({'title': 'Intensity & Feeling by sex',  'button': 'Data by sex',  'abscisseName': 'Sex of giver',  'orderedName': 'Intensity & feeling',  'data': getDataBySex(),  'dataError': ''})
	# Intensity & Feeling by age
	listHisto.append({'title': 'Intensity & Feeling by age',  'button': 'Data by age',  'orderedName': 'Intensity & feeling',  'abscisseName': 'Categories of age',  'data': getDataBySliceOfAge(),  'dataError': ''})
	# Intensity & Feeling by use of deodorant
	listHisto.append({'title': 'Intensity & Feeling by use of deodorant',  'button': 'Data by use of deodorant',  'orderedName': 'Intensity & feeling',  'abscisseName': 'Use of deodorant of giver',  'data': getDataByDeo(),  'dataError': ''})
	return listHisto


def createListPie():
	listPie = []
	# Repartition by sex
	listPie.append({'title': 'Repartition by sex', 'button': 'Pie by sex', 'description': 'Repartition by sex', 'data': pieByCritereSex()})
	# Repartition between slice of Age
	listPie.append({'title': 'Repartition between slice of Age', 'button': 'Pie by age', 'description': 'Repartition between slice of Age', 'data': pieByCritereSliceOfAge()})
	# Repartition by smoker
	listPie.append({'title': 'Repartition by smoker', 'button': 'Pie by smoking', 'description': 'Repartition by smoker', 'data': pieByCritereSmoker()})
	return listPie

def createListLines():
	listLines = []
	# Pleasanteness in function of intensity
	listLines.append({'title': 'Pleasanteness in function of intensity', 'button': 'Pleasanteness by intensity', 'abscisseName': 'Intensity', 'orderedName': 'Feeling', 'nameLine1': 'Raw data', 'dataLine1': intensityByFeeling(), 'nameLine2': 'Center data', 'dataLine2': intensityByFeelingCenter(), 'subtitle': ''})
	return listLines
