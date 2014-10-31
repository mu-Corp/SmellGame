#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django.db import models
from collections import defaultdict
import random
from math import sqrt

from SmellGuess.models   import *
from SmellGift.models    import *

################################################################
#######################    FUNCTIONS    ########################
################################################################

#todo doMoyForAllGivers():
def doMoyFeelingForAllGivers (givers) :
	moyenne = 0; somme = 0
	i=0
	for eachGiver in givers : 
		sample = Sample.objects.filter(sampleGiver_id=eachGiver.id)
		GuessByIdSample = Guess.objects.filter(sample_id=sample[0].id)
		if len(GuessByIdSample) != 0 :
			for elt in GuessByIdSample :
				if elt.intensity > 10 :
					somme += elt.feeling - 50
					i     += 1
	if i>0:
		moyenne = (somme* -1.0)/ i
	moyenne = round(moyenne,2)
	return moyenne

def errorFeelingForAllGivers(givers) :
	l_feeling = []
	for eachGiver in givers : 
		sample = Sample.objects.filter(sampleGiver_id=eachGiver.id)
		GuessByIdSample = Guess.objects.filter(sample_id=sample[0].id)
		if len(GuessByIdSample) != 0 :
			for elt in GuessByIdSample :
				if elt.intensity > 10 : l_feeling.append(50-elt.feeling)
	low,high = errorInterval(l_feeling)
	return [low,high]

def doMoyIntensityForAllGivers (givers) :
	moyenne = 0; somme = 0
	i=0
	for eachGiver in givers : 
		sample = Sample.objects.filter(sampleGiver_id=eachGiver.id)
		GuessByIdSample = Guess.objects.filter(sample_id=sample[0].id)
		if len(GuessByIdSample) != 0 :
			for elt in GuessByIdSample :
				if elt.intensity > 10 :
					somme += elt.intensity
					i     += 1
	if i>0:
		moyenne = (somme* 1.0)/ i
	moyenne = round(moyenne,2)
	return moyenne

def errorIntensityForAllGivers(givers) :
	l_intensity = []
	for eachGiver in givers : 
		sample = Sample.objects.filter(sampleGiver_id=eachGiver.id)
		GuessByIdSample = Guess.objects.filter(sample_id=sample[0].id)
		if len(GuessByIdSample) != 0 :
			for elt in GuessByIdSample :
				if elt.intensity > 10 : l_intensity.append(elt.intensity)
	low,high = errorInterval(l_intensity)
	return [low,high]


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
		if eachGuess.intensity < 10 :
			dictData["0-10"].append((float(eachGuess.feeling)-50)*-1.0)
		elif eachGuess.intensity < 20 :
			dictData["10-20"].append((float(eachGuess.feeling)-50)*-1.0)
		elif eachGuess.intensity < 30 :
			dictData["20-30"].append((float(eachGuess.feeling)-50)*-1.0)
		elif eachGuess.intensity < 40 :
			dictData["30-40"].append((float(eachGuess.feeling)-50)*-1.0)
		elif eachGuess.intensity < 50 :
			dictData["50-60"].append((float(eachGuess.feeling)-50)*-1.0)
		elif eachGuess.intensity < 60 :
			dictData["60-70"].append((float(eachGuess.feeling)-50)*-1.0)
		elif eachGuess.intensity < 70 :
			dictData["70-80"].append((float(eachGuess.feeling)-50)*-1.0)
		elif eachGuess.intensity < 80 :
			dictData["80-90"].append((float(eachGuess.feeling)-50)*-1.0)
		elif eachGuess.intensity < 90 :
			dictData["90-100"].append((float(eachGuess.feeling)-50)*-1.0)
	for eachKey in sorted(dictData.keys()) : 
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
	
def getRatio(Sub, All, dataNull = ()):
	ratio = 1.0 * len(Sub)  / (len(All)-len(dataNull))
	ratio = round(ratio,2)
	return ratio

def getFromTo(critere,fromNumber, toNumber):
	i=fromNumber
	fromTo = critere+" IN ("
	while i < toNumber : 
		fromTo += str(i)+","
		i += 1
	fromTo += str(i)+")"
	return fromTo

def intensitybyList(liste):
	listeToReturn = []
	for givers in liste : 
		listeToReturn.append(doMoyIntensityForAllGivers(givers))
	return listeToReturn

def feelingbyList(liste):
	listeToReturn = []
	for givers in liste : 
		listeToReturn.append(doMoyFeelingForAllGivers(givers))
	return listeToReturn


def mean_std_dev(l_durations):
    """ Calculate mean and standard deviation of data durations[]: """
    
    length, mean, std = len(l_durations), 0, 0
    
    for duration in l_durations:
        mean = mean + duration
    
    mean = mean / float(length)
    
    for duration in l_durations:
        std = std + (duration - mean) ** 2
    
    std = sqrt(std / float(length))
    mean = int(round(mean))
    std = int(round(std))
    
    return mean, std


#Intervalle de confiance à 95%:
def errorInterval(l_data):

    n = len(l_data)
    meanData, ecartType = mean_std_dev(l_data)
    
    demiLargeur = 1.96*(ecartType / sqrt(n))
    
    low = meanData - demiLargeur
    high = meanData + demiLargeur
    
    return low, high


###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__ == "__main__" :

	print 'Test in local\n.'
