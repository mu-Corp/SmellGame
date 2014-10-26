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
	if i>0:
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
	if i>0:
		moyenne = (somme* 1.0)/ i
	moyenne = round(moyenne,2)
	return moyenne


def getDataByDeo():
	giverWithDeo    = SampleGiver.objects.filter(deodorant = 1)
	giverWithoutDeo = SampleGiver.objects.filter(deodorant = 0)
	result = [
		['Moyenne des intensités des utilisateurs de déodorant',doMoyIntensityForAllGivers(giverWithDeo)],
		['Moyenne des apréciations des utilisateurs de déodorant',doMoyFeelingForAllGivers(giverWithDeo)],
		['Moyenne des intensités des non-utilisateurs de déodorant',doMoyIntensityForAllGivers(giverWithoutDeo)],
		['Moyenne des apréciations des non-utilisateurs de déodorant',doMoyFeelingForAllGivers(giverWithoutDeo)]
		]
	return result

def getDataBySex():
	giverWoman   = SampleGiver.objects.filter(sex = "F")
	giverMan = SampleGiver.objects.filter(sex = "M")
	result = [['Moyenne des intensités des hommes',doMoyIntensityForAllGivers(giverMan)],['Moyenne des apréciations des hommes',doMoyFeelingForAllGivers(giverMan)],['Moyenne des intensités des femmes',doMoyIntensityForAllGivers(giverWoman)],['Moyenne des apréciations des femmes',doMoyFeelingForAllGivers(giverWoman)]]
	return result

def getDataBySliceOfAge(): #todo
	dict_SliceOfAge = {}
	result = ()
	
	crit = "age"
	from_0_15   = SampleGiver.objects.extra(where=[getFromTo(crit, 0, 15)])
	from_16_30  = SampleGiver.objects.extra(where=[getFromTo(crit, 16, 30)])
	from_31_45  = SampleGiver.objects.extra(where=[getFromTo(crit, 31, 45)])
	from_46_60  = SampleGiver.objects.extra(where=[getFromTo(crit, 46, 60)])
	from_61_end = SampleGiver.objects.extra(where=[getFromTo(crit, 61, 125)])	
	
	dict_SliceOfAge["giver0_15"]   = SampleGiver.objects.extra(where=[getFromTo(crit, 0, 15)])
	dict_SliceOfAge["giver16_30"]  = SampleGiver.objects.extra(where=[getFromTo(crit, 16, 30)])
	dict_SliceOfAge["giver31_45"]  = SampleGiver.objects.extra(where=[getFromTo(crit, 31, 45)])
	dict_SliceOfAge["giver46_60"]  = SampleGiver.objects.extra(where=[getFromTo(crit, 46, 60)])
	dict_SliceOfAge["giver61_end"] = SampleGiver.objects.extra(where=[getFromTo(crit, 61, 125)])

	result = [
		["Intensité des donneurs de 0 à 15 ans ("+str(len(from_0_15))+")",   doMoyIntensityForAllGivers( dict_SliceOfAge["giver0_15"])],
		["Apréciations des donneurs de 0 à 15 ans ("+str(len(from_0_15))+")",   doMoyFeelingForAllGivers(   dict_SliceOfAge["giver0_15"])],
		["Intensité des donneurs de 16 à 30 ans ("+str(len(from_16_30))+")",  doMoyIntensityForAllGivers( dict_SliceOfAge["giver16_30"])],
		["Apréciations des donneurs de 16 à 30 ans ("+str(len(from_16_30))+")",  doMoyFeelingForAllGivers(   dict_SliceOfAge["giver16_30"])],
		["Intensités des donneurs de 31 à 45 ans ("+str(len(from_31_45))+")",  doMoyIntensityForAllGivers( dict_SliceOfAge["giver31_45"])],
		["Apréciations des donneurs de 31 à 45 ans ("+str(len(from_31_45))+")",  doMoyFeelingForAllGivers(   dict_SliceOfAge["giver31_45"])],
		["Intensités des donneurs de 46 à 60 ans ("+str(len(from_46_60))+")",  doMoyIntensityForAllGivers( dict_SliceOfAge["giver46_60"])],
		["Apréciations des donneurs de 46 à 60 ans ("+str(len(from_46_60))+")",  doMoyFeelingForAllGivers(   dict_SliceOfAge["giver46_60"])],
		["Intensités des donneurs sans données ("+str(len(from_61_end))+")", doMoyIntensityForAllGivers( dict_SliceOfAge["giver61_end"])],
		["Apréciations des donneurs sans données ("+str(len(from_61_end))+")",   doMoyFeelingForAllGivers(   dict_SliceOfAge["giver61_end"])] ]
	return result
	
def nameDataGraphPie(grph, fromNumb, toNumb, liste, y=""):
	string = ""
	if grph == 1:	
		string += str(y) + " de " + str(fromNumb) +" à "+str(toNumb) +" ans ("+str(len(liste))+")"
	elif grph == 2 :
		string += str(y) + str(fromNumb) +" à "+str(toNumb) +" ans ("+str(len(liste))+")"

	return string

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
	stringToReturn = [
		["Smoker("+str(len(giverTrue))+")",ratioTrue],
		["No smoker("+str(len(giverFalse))+")",ratioFalse],
		["empty field("+str(len(giverOther))+")",ratioOther]
	]
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
	stringToReturn = [["Woman ("+str(len(giverWoman))+")",ratioWoman],["Man ("+str(len(giverMan))+")",ratioMan]]
	return stringToReturn

def getFromTo(critere,fromNumber, toNumber):
	i=fromNumber
	fromTo = critere+" IN ("
	while i < toNumber : 
		fromTo += str(i)+","
		i += 1
	fromTo += str(i)+")"
	return fromTo
			
def pieByCritereSliceOfAge():
	#todo fix value of select
	crit = "age"
	from_0_15   = getFromTo(crit, 0, 15)
	from_16_30  = getFromTo(crit, 16, 30)
	from_31_45  = getFromTo(crit, 31, 45)
	from_46_60  = getFromTo(crit, 46, 60)
	from_61_end = getFromTo(crit, 61, 125)	
	
	allGiver    = SampleGiver.objects.all()
	giver0_15   = SampleGiver.objects.extra(where=[from_0_15])
	giver16_30  = SampleGiver.objects.extra(where=[from_16_30])
	giver31_45  = SampleGiver.objects.extra(where=[from_31_45])
	giver46_60  = SampleGiver.objects.extra(where=[from_46_60])
	giver61more = SampleGiver.objects.extra(where=[from_61_end])
	giverOther  = SampleGiver.objects.filter(age__isnull=True)
	
	ratio0_15   = getRatio(giver0_15,   allGiver, giverOther)
	ratio16_30  = getRatio(giver16_30,  allGiver, giverOther)
	ratio31_45  = getRatio(giver31_45,  allGiver, giverOther)
	ratio46_60  = getRatio(giver46_60,  allGiver, giverOther)
	ratio61more = getRatio(giver61more, allGiver, giverOther)
	ratioGiverOther = getRatio(giverOther, allGiver)
	stringToReturn = [
		["Ratio de 0 à 15 ans ("+str(len(giver0_15))+")",ratio0_15], 
		["Ratio de 16 à 30 ans ("+str(len(giver16_30))+")",ratio16_30], 
		["Ratio de 31 à 45 ans ("+str(len(giver31_45))+")",ratio31_45], 
		["Ratio de 46 à 60 ans ("+str(len(giver46_60))+")",ratio46_60],
		["Ratio de 61 ans & plus ("+str(len(giver61more))+")",ratio61more], 
		["Ratio des sans renseignements ("+str(len(giverOther))+")",ratioGiverOther]
		]
	return stringToReturn
	
################################################################
########################    CLASSES    #########################
################################################################

		
###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__ == "__main__" :

	print 'Test in local\n.'
