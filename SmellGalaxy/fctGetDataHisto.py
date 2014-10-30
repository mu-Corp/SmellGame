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

def getDataHistoByDeo(cas):
	giverWithDeo    = SampleGiver.objects.filter(deodorant = 1)
	giverWithoutDeo = SampleGiver.objects.filter(deodorant = 0)
		# cas = 1, intensité, sinon, cas =2 , feeling
	if cas == 'intensity':
	#
		result  = "[{"
		result += "name: 'Deodorant user'," 
		result += "data: ["+str(doMoyIntensityForAllGivers(giverWithDeo))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorIntensityForAllGivers(giverWithDeo))+"]},"
		result += "{name: 'Deodorant non-user',"
		result += "data: ["+ str(doMoyIntensityForAllGivers(giverWithoutDeo))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorIntensityForAllGivers(giverWithoutDeo))+"]}]"
		#result += ",\n["+boxplotIntensity(giverWithDeo) +","+ boxplotIntensity(giverWithoutDeo) + "]"	
	if cas == 'feeling':
	#
		result  = "[{"
		result += "name: 'Deodorant user',"  
		result += "data: ["+str(doMoyFeelingForAllGivers(giverWithDeo))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorFeelingForAllGivers(giverWithDeo))+"]},"
		result += "{name: 'Deodorant non-user'," 
		result += "data: ["+str(doMoyFeelingForAllGivers(giverWithoutDeo))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorFeelingForAllGivers(giverWithoutDeo))+"]}]"
		#result += ",\n["+ boxplotFeeling(giverWithDeo) +","+ boxplotFeeling(giverWithoutDeo) + "]"
	return result

def getBoxplotByDeo(cas):
	giverWithDeo    = SampleGiver.objects.filter(deodorant = 1)
	giverWithoutDeo = SampleGiver.objects.filter(deodorant = 0)
	if cas == 'intensity':
		result = "["+boxplotIntensity(giverWithDeo) +","+ boxplotIntensity(giverWithoutDeo) + "]"
	if cas == 'feeling':
		result = "["+boxplotFeeling(giverWithDeo) +","+ boxplotFeeling(giverWithoutDeo) + "]"
	return result

def getDataHistoBySex(cas):
	giverWoman   = SampleGiver.objects.filter(sex = "F")
	giverMan = SampleGiver.objects.filter(sex = "M")
	
		# cas = 1, intensité, sinon, cas =2 , feeling
	if cas == 'intensity':
	#
		result  = "[{name: 'Women',data: ["+str(doMoyIntensityForAllGivers(giverWoman))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorIntensityForAllGivers(giverWoman))+"]},"
		result += "{name: 'Men', data: ["+ str(doMoyIntensityForAllGivers(giverMan))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorIntensityForAllGivers(giverMan))+"]}]"
		#result += ",\n["+boxplotIntensity(giverMan) +","+ boxplotIntensity(giverWoman) + "]"
	if cas == 'feeling':
	#
		result  = "[{name: 'Women',data: ["+str(doMoyFeelingForAllGivers(giverWoman))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorFeelingForAllGivers(giverWoman))+"]},"
		result += "{name: 'Men', data: ["+ str(doMoyFeelingForAllGivers(giverMan))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorFeelingForAllGivers(giverMan))+"]}]"
		#result += ",\n["+boxplotFeeling(giverMan) +","+ boxplotFeeling(giverWoman) + "]"
		
	return result
	
def getBoxplotBySex(cas):
	giverWoman   = SampleGiver.objects.filter(sex = "F")
	giverMan = SampleGiver.objects.filter(sex = "M")
	if cas == 'intensity':
		result = "["+boxplotIntensity(giverMan) +","+ boxplotIntensity(giverWoman) + "]"
	if cas == 'feeling':
		result = "["+boxplotFeeling(giverMan) +","+ boxplotFeeling(giverWoman) + "]"
	return result

def getDataHistoBySmoker(cas):
	giverSmoker    = SampleGiver.objects.filter(smoker = True)
	giverNonSmoker = SampleGiver.objects.filter(smoker = False)
		# cas = 1, intensité, sinon, cas =2 , feeling
	if cas == 'intensity':
	#
		result  = "[{"
		result += "name: 'Non-Smokers'," 
		result += "data: ["+str(doMoyIntensityForAllGivers(giverNonSmoker))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorIntensityForAllGivers(giverNonSmoker))+"]},"
		result += "{name: 'Smokers',"
		result += "data: ["+ str(doMoyIntensityForAllGivers(giverSmoker))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorIntensityForAllGivers(giverSmoker))+"]}]"
		#result += ",\n["+boxplotIntensity(giverNonSmoker) +","+ boxplotIntensity(giverSmoker) + "]"	
	if cas == 'feeling':
	#
		result  = "[{"
		result += "name: 'Non-Smokers'," 
		result += "data: ["+str(doMoyFeelingForAllGivers(giverNonSmoker))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorFeelingForAllGivers(giverSmoker))+"]},"
		result += "{name: 'Smokers'," 
		result += "data: ["+ str(doMoyFeelingForAllGivers(giverSmoker))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorFeelingForAllGivers(giverNonSmoker))+"]}]"
		#result += ",\n["+ boxplotFeeling(giverNonSmoker) +","+ boxplotFeeling(giverSmoker) + "]"
	return result
	
def getBoxplotBySmoker(cas):
	giverSmoker    = SampleGiver.objects.filter(smoker = True)
	giverNonSmoker = SampleGiver.objects.filter(smoker = False)
	if cas == 'intensity':
		result = "["+boxplotIntensity(giverNonSmoker) +","+ boxplotIntensity(giverSmoker) + "]"	
	if cas == 'feeling':
		result = "["+ boxplotFeeling(giverNonSmoker) +","+ boxplotFeeling(giverSmoker) + "]"
	return result

def getDataHistoBySliceOfAge(cas): #todo
	dict_SliceOfAge = {}
	result = ()
	
	crit = "age"
	"""
	from_0_10   = SampleGiver.objects.extra(where=[getFromTo(crit, 0, 10)])
	from_11_20  = SampleGiver.objects.extra(where=[getFromTo(crit, 11, 20)])
	from_21_30  = SampleGiver.objects.extra(where=[getFromTo(crit, 21, 30)])
	from_31_40  = SampleGiver.objects.extra(where=[getFromTo(crit, 31, 40)])
	from_41_60  = SampleGiver.objects.extra(where=[getFromTo(crit, 41, 60)])	
	from_61_end = SampleGiver.objects.extra(where=[getFromTo(crit, 61, 125)])	
	"""
	
	dict_SliceOfAge["giver0_10"]   = SampleGiver.objects.extra(where=[getFromTo(crit, 0, 10)])
	dict_SliceOfAge["giver11_20"]  = SampleGiver.objects.extra(where=[getFromTo(crit, 11, 20)])
	dict_SliceOfAge["giver21_30"]  = SampleGiver.objects.extra(where=[getFromTo(crit, 21, 30)])
	dict_SliceOfAge["giver31_40"]  = SampleGiver.objects.extra(where=[getFromTo(crit, 31, 40)])
	dict_SliceOfAge["giver41_60"]  = SampleGiver.objects.extra(where=[getFromTo(crit, 41, 60)])	
	dict_SliceOfAge["giver61_end"] = SampleGiver.objects.extra(where=[getFromTo(crit, 61, 125)])
	for e in dict_SliceOfAge["giver41_60"] :
		print e.id
	if cas == 'intensity':
		# todo fix
		result  = "[{"
		result += "name: 'From 0 to 10 years old ("+str(len(dict_SliceOfAge["giver0_10"]))+")'," 
		result += "data: ["+str(doMoyIntensityForAllGivers(dict_SliceOfAge["giver0_10"]))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorIntensityForAllGivers(dict_SliceOfAge["giver0_10"]))+"]},"
		result += "{name: 'From 11 to 20 years old ("+str(len(dict_SliceOfAge["giver11_20"]))+")',"
		result += "data: ["+str(doMoyIntensityForAllGivers(dict_SliceOfAge["giver11_20"]))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorIntensityForAllGivers(dict_SliceOfAge["giver11_20"]))+"]},"
		result += "{name: 'From 21 to 30 years old ("+str(len(dict_SliceOfAge["giver21_30"]))+")'," 
		result += "data: ["+str(doMoyIntensityForAllGivers(dict_SliceOfAge["giver21_30"]))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorIntensityForAllGivers(dict_SliceOfAge["giver21_30"]))+"]},"
		result += "{name: 'From 31 to 40 years old ("+str(len(dict_SliceOfAge["giver31_40"]))+")'," 
		result += "data: ["+str(doMoyIntensityForAllGivers(dict_SliceOfAge["giver31_40"]))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorIntensityForAllGivers(dict_SliceOfAge["giver31_40"]))+"]},"
		result += "{name: 'From 41 to 60 years old ("+str(len(dict_SliceOfAge["giver41_60"]))+")', "
		result += "data: ["+str(doMoyIntensityForAllGivers(dict_SliceOfAge["giver41_60"]))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorIntensityForAllGivers(dict_SliceOfAge["giver41_60"]))+"]},"
		result += "{name: 'From 61 to 100 years old ("+str(len(dict_SliceOfAge["giver61_end"]))+")', "
		result += "data: ["+str(doMoyIntensityForAllGivers(dict_SliceOfAge["giver61_end"]))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorIntensityForAllGivers(dict_SliceOfAge["giver61_end"]))+"]}]"
		#result += ",\n["+ boxplotIntensity(dict_SliceOfAge["giver0_10"]) +","+ boxplotIntensity(dict_SliceOfAge["giver11_20"])+","+ boxplotIntensity(dict_SliceOfAge["giver21_30"])+","+ boxplotIntensity(dict_SliceOfAge["giver31_40"])+","+ boxplotIntensity(dict_SliceOfAge["giver41_60"])+","+ boxplotIntensity(dict_SliceOfAge["giver61_end"]) + "]"

	if cas == 'feeling':
		# todo fix
		result  = "[{"
		result += "name: 'From 0 to 10 years old ("+str(len(dict_SliceOfAge["giver0_10"]))+")'," 
		result += "data: ["+str(doMoyFeelingForAllGivers(dict_SliceOfAge["giver0_10"]))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorFeelingForAllGivers(dict_SliceOfAge["giver0_10"]))+"]},"
		result += "{name: 'From 11 to 20 years old ("+str(len(dict_SliceOfAge["giver11_20"]))+")',"
		result += "data: ["+str(doMoyFeelingForAllGivers(dict_SliceOfAge["giver11_20"]))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorFeelingForAllGivers(dict_SliceOfAge["giver11_20"]))+"]},"
		result += "{name: 'From 21 to 30 years old ("+str(len(dict_SliceOfAge["giver21_30"]))+")'," 
		result += "data: ["+str(doMoyFeelingForAllGivers(dict_SliceOfAge["giver21_30"]))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorFeelingForAllGivers(dict_SliceOfAge["giver21_30"]))+"]},"
		result += "{name: 'From 31 to 40 years old ("+str(len(dict_SliceOfAge["giver31_40"]))+")'," 
		result += "data: ["+str(doMoyFeelingForAllGivers(dict_SliceOfAge["giver31_40"]))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorFeelingForAllGivers(dict_SliceOfAge["giver31_40"]))+"]},"
		result += "{name: 'From 41 to 60 years old ("+str(len(dict_SliceOfAge["giver41_60"]))+")', "
		result += "data: ["+str(doMoyFeelingForAllGivers(dict_SliceOfAge["giver41_60"]))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorFeelingForAllGivers(dict_SliceOfAge["giver41_60"]))+"]},"
		result += "{name: 'From 61 to 100 years old ("+str(len(dict_SliceOfAge["giver61_end"]))+")', "
		result += "data: ["+str(doMoyFeelingForAllGivers(dict_SliceOfAge["giver61_end"]))+"]},"
		result += "{name: 'error', type: 'errorbar', data: ["+str(errorFeelingForAllGivers(dict_SliceOfAge["giver61_end"]))+"]}]"
		#result += ",\n["+ boxplotFeeling(dict_SliceOfAge["giver0_10"]) +","+ boxplotFeeling(dict_SliceOfAge["giver11_20"])+","+ boxplotFeeling(dict_SliceOfAge["giver21_30"])+","+ boxplotFeeling(dict_SliceOfAge["giver31_40"])+","+ boxplotFeeling(dict_SliceOfAge["giver41_60"])+","+ boxplotFeeling(dict_SliceOfAge["giver61_end"]) + "]"
	return result

def getBoxplotBySliceOfAge(cas):
	dict_SliceOfAge["giver0_10"]   = SampleGiver.objects.extra(where=[getFromTo(crit, 0, 10)])
	dict_SliceOfAge["giver11_20"]  = SampleGiver.objects.extra(where=[getFromTo(crit, 11, 20)])
	dict_SliceOfAge["giver21_30"]  = SampleGiver.objects.extra(where=[getFromTo(crit, 21, 30)])
	dict_SliceOfAge["giver31_40"]  = SampleGiver.objects.extra(where=[getFromTo(crit, 31, 40)])
	dict_SliceOfAge["giver41_60"]  = SampleGiver.objects.extra(where=[getFromTo(crit, 41, 60)])	
	dict_SliceOfAge["giver61_end"] = SampleGiver.objects.extra(where=[getFromTo(crit, 61, 125)])
	
	if cas == 'intensity':
		result  = "["+ boxplotIntensity(dict_SliceOfAge["giver0_10"]) +","+ boxplotIntensity(dict_SliceOfAge["giver11_20"])+","+ boxplotIntensity(dict_SliceOfAge["giver21_30"])+","+ boxplotIntensity(dict_SliceOfAge["giver31_40"])+","+ boxplotIntensity(dict_SliceOfAge["giver41_60"])+","+ boxplotIntensity(dict_SliceOfAge["giver61_end"]) + "]"
	if cas == 'feeling':
		result  = "["+ boxplotFeeling(dict_SliceOfAge["giver0_10"]) +","+ boxplotFeeling(dict_SliceOfAge["giver11_20"])+","+ boxplotFeeling(dict_SliceOfAge["giver21_30"])+","+ boxplotFeeling(dict_SliceOfAge["giver31_40"])+","+ boxplotFeeling(dict_SliceOfAge["giver41_60"])+","+ boxplotFeeling(dict_SliceOfAge["giver61_end"]) + "]"
	return result	

def getDataHistoByRegime(cas):
	#todo fix
	giverBroccoli       = SampleGiver.objects.filter(foodRecentlyEaten  = 1 )
	giverNotBroccoli    = SampleGiver.objects.filter( ).exclude(foodRecentlyEaten = 1 )
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

	listeComsommateur    = [giverBroccoli,    giverGabbage,    giverCauliflower,    giverAsparagus,    giverFish,    giverRed_meat,    giverFast_food,    giverSpicy_food,    giverAlcohol]
	listeNonComsommateur = [giverNotBroccoli, giverNotGabbage, giverNotCauliflower, giverNotAsparagus, giverNotFish, giverNotRed_meat, giverNotFast_food, giverNotSpicy_food, giverNotAlcohol]
	
	# cas = 1, intensité, sinon, cas =2 , feeling
	if cas == 'intensity':
		result =   "[{name: 'Intensity eaters', data:"        +str(intensitybyList(listeComsommateur))    +'},'
		result +=   "{name: 'error', type: 'errorbar', data: "+str(errorIntensitybyList(listeComsommateur))+"},"
		result +=   "{name: 'Intensity non-eaters', data:"    +str(intensitybyList(listeNonComsommateur)) +'},'
		result +=   "{name: 'error', type: 'errorbar', data: "+str(errorIntensitybyList(listeNonComsommateur))+"}]"
	if cas == 'feeling':
		result =    "[{name: 'Assessment eaters', data:"     +str(feelingbyList(listeComsommateur))     +'},'
		result +=   "{name: 'error', type: 'errorbar', data: "+str(errorFeelingbyList(listeComsommateur))+"},"
		result +=   "{name: 'Assessment non-eaters', data:" +str(feelingbyList(listeNonComsommateur))   +'},'
		result +=   "{name: 'error', type: 'errorbar', data: "+str(errorFeelingbyList(listeNonComsommateur))+"}]"
	
	#categories = ['Broccoli', 'Gabbage', 'Cauliflower', 'Asparagus', 'Fish', 'Red_meat', 'Fast_food', 'Spicy_food', 'Alcohol', 'Antibiotics']
	
	return result


###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__ == "__main__" :

	print 'Test in local\n.'
