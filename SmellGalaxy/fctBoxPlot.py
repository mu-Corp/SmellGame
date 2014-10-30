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
######################     BoxPlot     #########################
################################################################
def boxplotIntensity(givers):
	listVal = []
	boxPlot   = "[0.0, 0.0]"
	for eachGiver in givers : 
		GuessByIdSample = Guess.objects.filter(sample_id=eachGiver.id)
		if len(GuessByIdSample) != 0 :
			for elt in GuessByIdSample :
				if elt.intensity > 10 :
					listVal.append(elt.intensity)
	if len(listVal) > 4 :
	#doingBOxPlot
		#print listVal, 'sorted(listVal)', str(len(listVal)/4)
		listVal   = sorted(listVal)
		quart     = len(listVal)/4
		quartile1 = listVal[quart]
		quartile3 = listVal[len(listVal)-quart]
		boxPlot   = "["+str(quartile1)+", "+str(quartile3)+"]"
	return boxPlot
	
def boxplotFeeling(givers):
	listVal = []
	boxPlot   = "[0.0, 0.0]"
	for eachGiver in givers : 
		GuessByIdSample = Guess.objects.filter(sample_id=eachGiver.id)
		if len(GuessByIdSample) != 0 :
			for elt in GuessByIdSample :
				if elt.intensity > 10 :
					listVal.append((elt.feeling - 50)*-1.0)
	if len(listVal) > 4 :
	#doingBOxPlot
		#print listVal
		listVal   = sorted(listVal)
		quart     = len(listVal)/4
		quartile1 = listVal[quart]
		quartile3 = listVal[len(listVal)-quart]
		boxPlot= "["+str(quartile1)+", "+str(quartile3)+"]"
	return boxPlot
####	


###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__ == "__main__" :

	print 'Test in local\n.'
