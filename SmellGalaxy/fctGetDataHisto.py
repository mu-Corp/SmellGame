#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django.db import models
from collections import defaultdict
import random

from SmellGuess.models   import *
from SmellGift.models    import *
from fctMaths      import *
from fctBoxPlot    import *

################################################################
######################   FCT GetData   #########################
################################################################

def getDataHistoByDeo():
	giverWithDeo    = SampleGiver.objects.filter(deodorant = 1)
	giverWithoutDeo = SampleGiver.objects.filter(deodorant = 0)
	result  = "[{"
	result += "name: 'Utilisateurs de déodorant'," 
	result += "data: ["+str(doMoyIntensityForAllGivers(giverWithDeo))+", "+str(doMoyFeelingForAllGivers(giverWithDeo))+"]"
	result += "},{"
	result += "name: 'Non-utilisateurs de déodorant', "
	result += "data: ["+ str(doMoyIntensityForAllGivers(giverWithoutDeo))+", "+str(doMoyFeelingForAllGivers(giverWithoutDeo))+"]}]"	
	result += ",\n["+boxplotIntensity(giverWithDeo) +","+ boxplotFeeling(giverWithDeo) +","+ boxplotIntensity(giverWithoutDeo) +","+ boxplotFeeling(giverWithoutDeo) + "]"
	return result

def getDataHistoBySex():
	giverWoman   = SampleGiver.objects.filter(sex = "F")
	giverMan = SampleGiver.objects.filter(sex = "M")
	result  = "[{"
	result += "name: 'Hommes'," 
	result += "data: ["+str(doMoyIntensityForAllGivers(giverMan))+", "+str(doMoyFeelingForAllGivers(giverMan))+"]"
	result += "},{"
	result += "name: 'Femmes', "
	result += "data: ["+ str(doMoyIntensityForAllGivers(giverWoman))+", "+str(doMoyFeelingForAllGivers(giverWoman))+"]}]"
	result += ",\n["+boxplotIntensity(giverMan) +","+ boxplotFeeling(giverMan) +","+ boxplotIntensity(giverWoman) +","+ boxplotFeeling(giverWoman) + "]"
	return result


def getDataHistoBySmoker():
	giverSmoker    = SampleGiver.objects.filter(smoker = True)
	giverNonSmoker = SampleGiver.objects.filter(smoker = False)
	result  = "[{"
	result += "name: 'Non fumeurs'," 
	result += "data: ["+str(doMoyIntensityForAllGivers(giverNonSmoker))+", "+str(doMoyFeelingForAllGivers(giverNonSmoker))+"]"
	result += "},{"
	result += "name: 'Fumeurs', "
	result += "data: ["+ str(doMoyIntensityForAllGivers(giverSmoker))+", "+str(doMoyFeelingForAllGivers(giverSmoker))+"]}]"
	result += ",\n["+boxplotIntensity(giverNonSmoker) +","+ boxplotFeeling(giverNonSmoker) +","+ boxplotIntensity(giverSmoker) +","+ boxplotFeeling(giverSmoker) + "]"
	return result


def getDataHistoBySliceOfAge(): #todo
	dict_SliceOfAge = {}
	result = ()
	
	crit = "age"
	from_0_10   = SampleGiver.objects.extra(where=[getFromTo(crit, 0, 10)])
	from_11_20  = SampleGiver.objects.extra(where=[getFromTo(crit, 11, 20)])
	from_21_30  = SampleGiver.objects.extra(where=[getFromTo(crit, 21, 30)])
	from_31_40  = SampleGiver.objects.extra(where=[getFromTo(crit, 31, 40)])
	from_41_end = SampleGiver.objects.extra(where=[getFromTo(crit, 41, 125)])	
	
	dict_SliceOfAge["giver0_10"]   = SampleGiver.objects.extra(where=[getFromTo(crit, 0, 10)])
	dict_SliceOfAge["giver11_20"]  = SampleGiver.objects.extra(where=[getFromTo(crit, 11, 20)])
	dict_SliceOfAge["giver21_30"]  = SampleGiver.objects.extra(where=[getFromTo(crit, 21, 30)])
	dict_SliceOfAge["giver31_40"]  = SampleGiver.objects.extra(where=[getFromTo(crit, 31, 40)])
	dict_SliceOfAge["giver41_end"] = SampleGiver.objects.extra(where=[getFromTo(crit, 41, 125)])
	# todo fix
	result  = "[{"
	result += "name: 'De 0 à 10 ans ("+str(len(from_0_10))+")'," 
	result += "data: ["+str(doMoyIntensityForAllGivers(dict_SliceOfAge["giver0_10"]))+", "+str(doMoyFeelingForAllGivers(dict_SliceOfAge["giver0_10"]))+"]"
	result += "},{"
	result += "name: 'De 11 à 20 ans ("+str(len(from_11_20))+")',"
	result += "data: ["+str(doMoyIntensityForAllGivers(dict_SliceOfAge["giver11_20"]))+", "+str(doMoyFeelingForAllGivers(dict_SliceOfAge["giver11_20"]))+"]"
	result += "},{"
	result += "name: 'De 21 à 30 ans ("+str(len(from_21_30))+")'," 
	result += "data: ["+str(doMoyIntensityForAllGivers(dict_SliceOfAge["giver21_30"]))+", "+str(doMoyFeelingForAllGivers(dict_SliceOfAge["giver21_30"]))+"]"
	result += "},{"
	result += "name: 'De 31 à 40 ans ("+str(len(from_31_40))+")'," 
	result += "data: ["+str(doMoyIntensityForAllGivers(dict_SliceOfAge["giver31_40"]))+", "+str(doMoyFeelingForAllGivers(dict_SliceOfAge["giver31_40"]))+"]"
	result += "},{"
	result += "name: 'De 41 à 100 ans ("+str(len(from_41_end))+")', "
	result += "data: ["+ str(doMoyIntensityForAllGivers(dict_SliceOfAge["giver41_end"]))+", "+str(doMoyFeelingForAllGivers(dict_SliceOfAge["giver41_end"]))+"]}]"
	result += ",\n["+ boxplotIntensity(dict_SliceOfAge["giver0_10"]) +","+ boxplotFeeling(dict_SliceOfAge["giver0_10"])
	result += ","+    boxplotFeeling(dict_SliceOfAge["giver11_20"])  +","+ boxplotFeeling(dict_SliceOfAge["giver11_20"])
	result += ","+    boxplotFeeling(dict_SliceOfAge["giver21_30"])  +","+ boxplotFeeling(dict_SliceOfAge["giver21_30"])
	result += ","+    boxplotFeeling(dict_SliceOfAge["giver31_40"])  +","+ boxplotFeeling(dict_SliceOfAge["giver31_40"])
	result += ","+    boxplotFeeling(dict_SliceOfAge["giver41_end"]) +","+ boxplotFeeling(dict_SliceOfAge["giver41_end"]) + "]"
	return result
	
def getDataHistoByRegime(cas):
	#todo fix
	giverBroccoli       = SampleGiver.objects.filter(foodRecentlyEaten  = 1 )
	giverNotBroccoli    = SampleGiver.objects.filter( ).exclude(foodRecentlyEaten = 1 )
	print len(SampleGiver.objects.all()), len(giverBroccoli), len(giverNotBroccoli)
	giverGabbage        = SampleGiver.objects.filter(foodRecentlyEaten  = 2 )
	giverNotGabbage     = SampleGiver.objects.filter( ).exclude(foodRecentlyEaten = 2)
	giverCauliflower    = SampleGiver.objects.filter(foodRecentlyEaten  = 3 )
	giverNotCauliflower = SampleGiver.objects.filter( ).exclude(foodRecentlyEaten = 3)
	giverAsparagus      = SampleGiver.objects.filter(foodRecentlyEaten  = 4 )
	giverNotAsparagus   = SampleGiver.objects.filter( ).exclude(foodRecentlyEaten = 4)
	giverFish           = SampleGiver.objects.filter(foodRecentlyEaten  = 5 )
	giverNotFish        = SampleGiver.objects.filter( ).exclude(foodRecentlyEaten = 5)
	giverRed_meat       = SampleGiver.objects.filter(foodRecentlyEaten  = 6 )
	giverNotRed_meat    = SampleGiver.objects.filter( ).exclude(foodRecentlyEaten = 6)
	giverFast_food      = SampleGiver.objects.filter(foodRecentlyEaten  = 7 )
	giverNotFast_food   = SampleGiver.objects.filter( ).exclude(foodRecentlyEaten = 7)
	giverSpicy_food     = SampleGiver.objects.filter(foodRecentlyEaten  = 8 )
	giverNotSpicy_food  = SampleGiver.objects.filter( ).exclude(foodRecentlyEaten = 8)
	giverAlcohol        = SampleGiver.objects.filter(foodRecentlyEaten  = 9 )
	giverNotAlcohol     = SampleGiver.objects.filter( ).exclude(foodRecentlyEaten = 9)
	giverAntibiotics    = SampleGiver.objects.filter(foodRecentlyEaten  = 10 )
	giverNotAntibiotics = SampleGiver.objects.filter( ).exclude(foodRecentlyEaten = 10)

	listeComsommateur    = [giverBroccoli,    giverGabbage,    giverCauliflower,    giverAsparagus,    giverFish,    giverRed_meat,    giverFast_food,    giverSpicy_food,    giverAlcohol,    giverAntibiotics]
	listeNonComsommateur = [giverNotBroccoli, giverNotGabbage, giverNotCauliflower, giverNotAsparagus, giverNotFish, giverNotRed_meat, giverNotFast_food, giverNotSpicy_food, giverNotAlcohol, giverAntibiotics]
	
	# cas = 1, intensité, sinon, cas =2 , feeling
	if cas == 'intensity':
		result =   "[{name: 'Intensités mangeur', data:"        +str(intensitybyList(listeComsommateur))    +'},'
		result +=   "{name: 'Intensités non-mangeur', data:"    +str(intensitybyList(listeNonComsommateur)) +'}]'
	if cas == 'feeling':
		result =    "[{name: 'Appréciations mangeur', data:"     +str(feelingbyList(listeComsommateur))     +'},'
		result +=   "{name: 'Appréciations non-mangeur', data:" +str(feelingbyList(listeNonComsommateur))   +'}]'
	categories = ['Broccoli', 'Gabbage', 'Cauliflower', 'Asparagus', 'Fish', 'Red_meat', 'Fast_food', 'Spicy_food', 'Alcohol', 'Antibiotics']
	
	return result


###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__ == "__main__" :

	print 'Test in local\n.'