#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django.db import models
from collections import defaultdict
import random

from SmellGuess.models   import *
from SmellGift.models    import *

################################################################
#######################    FUNCTIONS    ########################
################################################################
#Plus utils
def getSmeller(givers): 
	i = 0
	for eachGiver in givers : 
		#print "Giver Infos :", eachGiver.id
		GuessByIdSample = Guess.objects.filter(sample_id=eachGiver.id)
		moyIntensity = doMoyenneIntensity(GuessByIdSample)
		moyFeeling   = doMoyenneFeeling(GuessByIdSample)
		i += len(GuessByIdSample)
		#print "Moyenne intensité - ", doMoyenneIntensity(GuessByIdSample)
		#print "Moyenne feeling   - ", doMoyenneFeeling(GuessByIdSample)
		#print "\n--------------"
	print "total ech : ", i

#todo doMoyForAllGivers():
def doMoyFeelingForAllGivers (givers) :
	moyenne = 0; somme = 0
	i=0
	for eachGiver in givers : 
		GuessByIdSample = Guess.objects.filter(sample_id=eachGiver.id)
		if len(GuessByIdSample) != 0 :
			for elt in GuessByIdSample :
				somme += elt.feeling
				i     += 1
	moyenne = (somme* 1.0)/ i
	moyenne = round(moyenne,2)
	return moyenne

def doMoyIntensityForAllGivers (givers) :
	moyenne = 0; somme = 0
	i=0
	for eachGiver in givers : 
		GuessByIdSample = Guess.objects.filter(sample_id=eachGiver.id)
		if len(GuessByIdSample) != 0 :
			for elt in GuessByIdSample :
				somme += elt.intensity
				i     += 1
	moyenne = (somme* 1.0)/ i
	moyenne = round(moyenne,2)
	return moyenne


def getDataByDeo():
	giverWithDeo    = SampleGiver.objects.filter(deodorant = 1)
	giverWithoutDeo = SampleGiver.objects.filter(deodorant = 0)
	result = [['People who use deo - intensity',doMoyIntensityForAllGivers(giverWithDeo)],['People who use deo - feeling',doMoyFeelingForAllGivers(giverWithDeo)],['People who not use deo - intensity',doMoyIntensityForAllGivers(giverWithoutDeo)],['People who not use deo - feeling',doMoyFeelingForAllGivers(giverWithoutDeo)]]
	return result

def getDataBySex():
	giverWoman   = SampleGiver.objects.filter(sex = "F")
	giverMan = SampleGiver.objects.filter(sex = "M")
	result = [['Man people - intensity',doMoyIntensityForAllGivers(giverMan)],['Man people - feeling',doMoyFeelingForAllGivers(giverMan)],['Woman people - intensity',doMoyIntensityForAllGivers(giverWoman)],['Woman people - feeling',doMoyFeelingForAllGivers(giverWoman)]]
	return result

def getDataBySliceOfAge(): #todo
	dict_SliceOfAge = {}
	result = ()
	
	dict_SliceOfAge["giver0_15"]   = SampleGiver.objects.extra( select = {'ofSlice': "age > '0' & age < 16"})
	dict_SliceOfAge["giver15_30"]  = SampleGiver.objects.extra( select = {'ofSlice': "age > '15' & age < 31"})
	dict_SliceOfAge["giver30_60"]  = SampleGiver.objects.extra( select = {'ofSlice': "age > '30' & age < 61"})
	dict_SliceOfAge["giver60more"] = SampleGiver.objects.extra( select = {'ofSlice': "age > '60'"})

	result = [
		["giver0_15_Intensity",   doMoyIntensityForAllGivers( dict_SliceOfAge["giver0_15"])],
		['giver0_15_feeling',     doMoyFeelingForAllGivers(   dict_SliceOfAge["giver0_15"])],
		["giver15_30_Intensity",  doMoyIntensityForAllGivers( dict_SliceOfAge["giver15_30"])],
		['giver15_30_feeling',    doMoyFeelingForAllGivers(   dict_SliceOfAge["giver15_30"])],
		["giver30_60_Intensity",  doMoyIntensityForAllGivers( dict_SliceOfAge["giver30_60"])],
		['giver30_60_feeling',    doMoyFeelingForAllGivers(   dict_SliceOfAge["giver30_60"])],
		["giver60more_Intensity", doMoyIntensityForAllGivers( dict_SliceOfAge["giver60more"])],
		['giver60more_feeling',   doMoyFeelingForAllGivers(   dict_SliceOfAge["giver60more"])] ]
	
	return result

def intensityByFeeling():
	allGuess = Guess.objects.all()
	dictData= defaultdict(lambda:list())
	string = []
	for eachGuess in allGuess :
		dictData[eachGuess.intensity].append((int(eachGuess.feeling)))
	for eachKey in dictData.keys() : 
		string.append([str(eachKey), moyList(dictData[eachKey])])
	return string
	
def intensityByFeelingCenter():
	allGuess = Guess.objects.all()
	dictData= defaultdict(lambda:list())
	string = []
	for eachGuess in allGuess :
		dictData[eachGuess.intensity].append((int(eachGuess.feeling)-50))
	for eachKey in dictData.keys() : 
		string.append([str(eachKey), moyList(dictData[eachKey])])
	return string
	
def moyList(aList):
	moyenne = 0.0; somme = 0.0
	if len(aList) > 0 : 
		for elt in aList : 
			somme += elt
		moyenne = somme / len(aList)
	moyenne = round(moyenne,2)
	return moyenne


def pieByCritereSmoker():
	allGiver    = SampleGiver.objects.all()
	giverTrue   = SampleGiver.objects.filter(smoker = True)
	giverFalse  = SampleGiver.objects.filter(smoker = False)
	giverOther  = SampleGiver.objects.filter(smoker__isnull=True)
	
	ratioTrue  = getRatio(giverTrue, allGiver)
	ratioFalse = getRatio(giverFalse, allGiver)
	ratioOther = getRatio(giverOther, allGiver)
	stringToReturn = [['Smoker',ratioTrue],['No smoker',ratioFalse],['empty field',ratioOther]]
	return stringToReturn

def getRatio(Sub, All, dataNull = ()):
	ratio = 1.0 * len(Sub)  / (len(All)-len(dataNull))
	ratio = round(ratio,2)
	return ratio

def pieByCritereSex():
	allGiver   = SampleGiver.objects.all()
	giverWoman = SampleGiver.objects.filter(sex = "F")
	giverMan   = SampleGiver.objects.filter(sex = "M")
	giverOther = SampleGiver.objects.filter(sex__isnull=True)
	
	ratioWoman = getRatio(giverWoman, allGiver, giverOther)
	ratioMan   = getRatio(giverMan,   allGiver, giverOther)
	stringToReturn = [['Woman',ratioWoman],['Man',ratioMan]]
	return stringToReturn
	
def pieByCritereSliceOfAge():
	#todo fix value of select
	allGiver    = SampleGiver.objects.all()
	giver0_15   = SampleGiver.objects.extra( select = {'ofSlice': "age > '0' & age < 16"})
	giver15_30  = SampleGiver.objects.extra( select = {'ofSlice': "age > '15' & age < 31"})
	giver30_60  = SampleGiver.objects.extra( select = {'ofSlice': "age > '30' & age < 61"})
	giver60more = SampleGiver.objects.extra( select = {'ofSlice': "age > '60'"})
	giverOther  = SampleGiver.objects.filter(age__isnull=True)
	
	ratio0_15   = getRatio(giver0_15,   allGiver, giverOther)
	ratio15_30  = getRatio(giver15_30,  allGiver, giverOther)
	ratio30_60  = getRatio(giver30_60,  allGiver, giverOther)
	ratio60more = getRatio(giver60more, allGiver, giverOther)
	stringToReturn = [['ratio0_15',ratio0_15],['ratio15_30',ratio15_30],['ratio30_60',ratio30_60],['ratio60more',ratio60more]]
	return stringToReturn
	
################################################################
########################    CLASSES    #########################
################################################################

class GraphHistogramme(models.Model):
	id           = models.AutoField(primary_key=True)
	title        = models.CharField(max_length=8096)
	button       = models.CharField(max_length=8096)
	orderedName  = models.CharField(max_length=256)
	abscisseName = models.CharField(max_length=256)
	data         = models.CharField(max_length=8096)
	dataError    = models.CharField(max_length=8096)
	#graphHisto = GraphHistogramme(title="", button="", orderedName="", abscisseName="", data=getdata...(), dataError =getdata...())


class GraphPie(models.Model):
	id          = models.AutoField(primary_key=True)
	title       = models.CharField(max_length=512)
	button      = models.CharField(max_length=512)
	description = models.CharField(max_length=512)
	data        = models.CharField(max_length=8096)
	#graph= GraphPie(title="", button="", description="", data=getdata...())

class GraphLines(models.Model):
	id          = models.AutoField(primary_key=True)
	title          = models.CharField(max_length=320)
	subtitle       = models.CharField(max_length=320)
	button         = models.CharField(max_length=320)
	abscisseName   = models.CharField(max_length=256)
	orderedName    = models.CharField(max_length=256)
	nameLine1  = models.CharField(max_length=256)
	dataLine1  = models.CharField(max_length=8096)
	nameLine2  = models.CharField(max_length=256)
	dataLine2  = models.CharField(max_length=8096)
	#graphLines = GraphLines(title="", button="", abscisseName="", orderedName="", nameLine1="",dataLine1=getdata...(), nameLine2="", dataLine2 =getdata...())
		
###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__ == "__main__" :

	print 'Test in local\n.'

	print 'Test By Deo\n'
	print getDataByDeo()
	
	print 'Test in Sex\n'
	print getDataBySex()
	
	print 'Test in Sex\n'
	print getDataBySliceOfAge()
