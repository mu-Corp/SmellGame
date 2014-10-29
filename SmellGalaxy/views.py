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
	#SetOptionHisto(titre, y, indicationCurseur, cat, donnees, erreur, soustitre) 
	listHisto = []
	
	cat1 = ['Intensités','Appréciations']
	cat2 = ['Broccoli', 'Gabbage', 'Cauliflower', 'Asparagus', 'Fish', 'Red_meat', 'Fast_food', 'Spicy_food', 'Alcohol', 'Antibiotics']
	# Intensity & Feeling by sex
	listHisto.append({'title': 'Intensités & apréciations selon le sexe',  'button': 'Données selon le sexe',  'abscisseName': 'Sexe du donneur',  'orderedName': 'Intensités & apréciations',  'data': getDataHistoBySex(),  'dataError': '', 'categories' : cat1})
	# Intensity & Feeling by age
	listHisto.append({'title': 'Intensités & apréciations selon l âge',  'button': 'Données selon l\'âge',  'orderedName': 'Intensités & apréciations',  'abscisseName': 'Tranche d âge',  'data': getDataHistoBySliceOfAge(),  'dataError': '', 'categories' : cat1 })
	# Intensity & Feeling by use of deodorant
	listHisto.append({'title': 'Intensités & apréciations selon l utilisation de déodorant',  'button': 'Données déodorant',  'orderedName': 'Intensités & apréciations',  'abscisseName': 'Utilisation de déodorant',  'data': getDataHistoByDeo(),  'dataError': '', 'categories' : cat1})
	# Intensity & Feeling by Smoking
	listHisto.append({'title': 'Intensités & apréciations selon la comsommation de cigarettes',  'button': 'Données fumeur',  'orderedName': 'Intensités & apréciations',  'abscisseName': 'Comsommation de cigarettes',  'data': getDataHistoBySmoker(),  'dataError': '', 'categories' : cat1 })
	
	# Intensity by Recently eaten
	listHisto.append({'title': 'Intensités selon la comsommation d aliments',  'button': 'Intensité selon l\'alimentation',  'orderedName': 'Intensités',  'abscisseName': 'Comsommation de cigarettes',  'data': getDataHistoByRegime('intensity'),  'dataError': '', 'categories' : cat2 })
	# Feeling by Recently eaten
	listHisto.append({'title': 'Apréciations selon la comsommation d aliments',  'button': 'Feeling selon l\'alimentation',  'orderedName': 'Appréciations',  'abscisseName': 'Comsommation de cigarettes',  'data': getDataHistoByRegime('feeling'),  'dataError': '', 'categories' : cat2 })
	
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

def createListLines():
	listLines = []
	# Pleasanteness in function of intensity
	listLines.append({'title': "Apréciation en fonction de l intensité", 'button': 'Apréciation par l intensité', 'abscisseName': 'Intensité', 'orderedName': 'Apréciation', 'nameLine1': 'Données brutes', 'dataLine1': "[]", 'nameLine2': 'Données centrées', 'dataLine2': intensityByFeelingCenter(), 'subtitle': ''})
	return listLines
