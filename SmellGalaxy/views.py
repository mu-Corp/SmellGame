#-*- coding: utf-8 -*-

"""
Authors: 
- Florian Thonier, florian.thonier@gmail.com (2014)
- Nathan Foulquier, nathan.foulquier.pro@gmail.com (2014)
- Jean Coquet, coquet.jean@gmail.com (2014)
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

cat1 = [['Intensités (0~100)'],['Appréciations (-50~50)']]
cat2 = ['Broccoli', 'Gabbage', 'Cauliflower', 'Asparagus', 'Fish', 'Red meat', 'Fast food', 'Spicy food', 'Alcohol', 'Antibiotics']
################################################################
#########################    VIEWS    ##########################
################################################################


# Nathan view
def graphesView(request):
    paramToGenerateTemplate = dict()
    paramToGenerateTemplate['HistoGraphs']    = createListHisto()
    paramToGenerateTemplate['HistoGraphsRE']  = createListHistoRE()
    paramToGenerateTemplate['PiesGraphs']     = createListPie()
    paramToGenerateTemplate['PiesGraphsRE']   = createListPieRecentlyEaten()
    paramToGenerateTemplate['LinesGraphs']    = createListLines()

    return render(request, 'SmellGalaxyTemplate/Graphes.html', paramToGenerateTemplate) 
    
   
def createListHisto():
	#SetOptionHisto(titre, y, indicationCurseur, cat, donnees, erreur, soustitre) 
	listHisto = []
	
	cat1 = ['Intensités (0~100)','Appréciations (-50~50)']
	cat2 = ['Broccoli', 'Gabbage', 'Cauliflower', 'Asparagus', 'Fish', 'Red_meat', 'Fast_food', 'Spicy_food', 'Alcohol', 'Antibiotics']
	# Intensity & Feeling by sex
	listHisto.append({
		'button': 'Données selon le sexe', 'abscisseName': 'Sexe du donneur', 'description': '',
		'titleLeft' : 'Intensités selon le sexe',     'orderedNameLeft' : 'Intensités (0~100)', 'categoriesLeft' : cat1[0],     'dataLeft' : getDataHistoBySex('intensity'),  'dataErrorLeft': '',
		'titleRight': 'Appréciations selon le sexe',  'orderedNameRight': 'Appréciations (-50~50)', 'categoriesRight' : cat1[1], 'dataRight': getDataHistoBySex('feeling'),  'dataErrorRight': ''})
	# Intensity & Feeling by age
	listHisto.append({
		'button': 'Données selon l\'âge', 'abscisseName': 'Tranche d âge', 'description': '',
		'titleLeft': 'Intensités selon l âge',    'orderedNameLeft': 'Intensités (0~100)', 'categoriesLeft' : cat1[0], 'dataLeft': getDataHistoBySliceOfAge('intensity'),  'dataErrorLeft': '',
		'titleRight': 'Appréciations selon l âge',  'orderedNameRight': 'Apréciations', 'categoriesRight' : cat1[1], 'dataRight': getDataHistoBySliceOfAge('feeling'),  'dataErrorRight': ''})
	# Intensity & Feeling by use of deodorant
	listHisto.append({
		'button': 'Données déodorant',  'abscisseName': 'Utilisation de déodorant',  'description': '',
		'titleLeft': 'Intensités selon l utilisation de déodorant',    'orderedNameLeft': 'Intensités (0~100)',  'categoriesLeft' : cat1[0], 'dataLeft': getDataHistoByDeo('intensity'),  'dataErrorLeft': '', 
		'titleRight': 'Appréciations selon l utilisation de déodorant',  'orderedNameRight': 'Appréciations (-50~50)', 'categoriesRight' : cat1[1], 'dataRight': getDataHistoByDeo('feeling'),  'dataErrorRight': ''})
	# Intensity & Feeling by Smoking
	listHisto.append({
		'button': 'Données fumeur', 'abscisseNameLeft': 'Comsommation de cigarettes', 'description': '',
		'titleLeft': 'Intensités selon la comsommation de cigarettes',   'orderedNameLeft': 'Intensités (0~100)', 'categoriesLeft' : cat1[0],   'dataLeft': getDataHistoBySmoker('intensity'),  'dataErrorLeft': '', 
		'titleRight': 'Appréciations selon la comsommation de cigarettes', 'orderedNameRight': 'Appréciations (-50~50)', 'categoriesRight' : cat1[1], 'dataRight': getDataHistoBySmoker('feeling'),  'dataErrorRight': ''})

	return listHisto

def createListHistoRE():
	#SetOptionHisto(titre, y, indicationCurseur, cat, donnees, erreur, soustitre) 
	listHisto = []
	# Intensity by Recently eaten
	listHisto.append({
		'button': 'Données selon l\'alimentation', 'abscisseNameLeft': 'Comsommation de cigarettes', 
		'titleLeft': 'Intensités selon la consommation d aliments',   'orderedNameLeft': 'Intensités (0~100)',  'categoriesLeft' : cat2,  'dataLeft': getDataHistoByRegime('intensity'),  'dataErrorLeft': '', 
		'titleRight': 'Appréciations selon la consommation d aliments',    'orderedNameRight': 'Appréciations (-50~50)',   'categoriesRight' : cat2,  'dataRight': getDataHistoByRegime('feeling'),  'dataErrorRight': ''})

	return listHisto


def createListPie():
	listPie = []
	# Repartition by sex
	listPie.append({'title': 'Repartition selon le sexe', 'button': 'Sexe des donneurs', 'description': '', 'data': pieByCritereSex()})
	# Repartition between slice of Age
	listPie.append({'title': 'Repartition selon la tranche d âge', 'button': 'Tranche d âge', 'description': '', 'data': pieByCritereSliceOfAge()})
	# Repartition by smoker
	listPie.append({'title': 'Répartition par consommation de cigarettes', 'button': 'Consommation de cigarettes', 'description': '', 'data': pieByCritereSmoker()})
	return listPie

def createListPieRecentlyEaten():
	listPie = []
	for i in range(1,11,1):
		listPie.append({'title': 'Repartition by recent '+cat2[i-1]+' consumption', 'button': cat2[i-1]+' recenty eaten', 'description': '', 'data': pieByCritereRecentlyEaten(i)})
	return listPie

def createListLines():
	listLines = []
	# Pleasanteness in function of intensity
	listLines.append({'title': "Apréciation en fonction de l intensité", 'button': 'Apréciation par l intensité', 'abscisseName': 'Intensités (0~100)', 'orderedName': 'Apréciation', 'nameLine1': 'Données brutes', 'dataLine1': "[]", 'nameLine2': 'Données centrées', 'dataLine2': intensityByFeelingCenter(), 'subtitle': ''})
	return listLines
