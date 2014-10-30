#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django.db import models
from collections import defaultdict
import random

from django.utils.translation import ugettext_lazy as _

from SmellGuess.models   import *
from SmellGift.models    import *
from fctMaths      import *
from fctBoxPlot    import *

################################################################
######################   FCT GetData   #########################
################################################################

def pieByCritereSmoker():
	allGiver    = SampleGiver.objects.all()
	giverTrue   = SampleGiver.objects.filter(smoker = True)
	giverFalse  = SampleGiver.objects.filter(smoker = False)
	giverOther  = SampleGiver.objects.filter(smoker__isnull=True)
	
	ratioTrue  = getRatio(giverTrue, allGiver)
	ratioFalse = getRatio(giverFalse, allGiver)
	ratioOther = getRatio(giverOther, allGiver)
	stringToReturn = [
		[str(_(u"Fumeurs("))+str(len(giverTrue))+")",ratioTrue],
		[str(_(u"Non fumeurs("))+str(len(giverFalse))+")",ratioFalse]
		#,["empty field("+str(len(giverOther))+")",ratioOther]
	]
	return stringToReturn


def pieByCritereSex():
	allGiver   = SampleGiver.objects.all()
	giverWoman = SampleGiver.objects.filter(sex = "F")
	giverMan   = SampleGiver.objects.filter(sex = "M")
	giverOther = SampleGiver.objects.filter(sex__isnull=True)
	
	ratioWoman = getRatio(giverWoman, allGiver, giverOther)
	ratioMan   = getRatio(giverMan,   allGiver, giverOther)
	stringToReturn = [
		[str(_(u"Femme ("))+str(len(giverMan))+")",ratioMan],
		[str(_(u"Homme ("))+str(len(giverWoman))+")",ratioWoman]
		]
	return stringToReturn
def pieByCritereRecentlyEaten(elt):

	allGiver   = SampleGiver.objects.all()
	giverRE       = SampleGiver.objects.filter(foodRecentlyEaten  = elt )
	giverNotRE    = SampleGiver.objects.filter( ).exclude(foodRecentlyEaten = elt )


	categories = [_(u'Brocoli'), _(u'Chou'), _(u'Chou fleur'), _(u'Asperge'), _(u'Poisson'), _(u'Viande rouge'), _(u'Fast food'), _(u'Epicé'), _(u'Alcool'), _(u'Antibiotiques')]
	ratioRE    = getRatio( giverRE,      allGiver )
	ratioNotRE = getRatio( giverNotRE,   allGiver )
	stringToReturn = [
		[categories[elt-1]+ str(_(u" récemment mangé ("))+str(len(giverRE))+")",ratioRE],
		[categories[elt-1]+ str(_(u" pas récemment ("))+str(len(giverNotRE))+")",ratioNotRE]
		]
	return stringToReturn

			
def pieByCritereSliceOfAge():
	#todo fix value of select
	crit = "age"
	from_0_10   = getFromTo(crit, 0, 10)
	from_11_20  = getFromTo(crit, 11, 20)
	from_21_30  = getFromTo(crit, 21, 30)
	from_31_40  = getFromTo(crit, 31, 40)
	from_41_end = getFromTo(crit, 41, 125)	
	
	allGiver    = SampleGiver.objects.all()
	giver0_10   = SampleGiver.objects.extra(where=[from_0_10])
	giver11_20  = SampleGiver.objects.extra(where=[from_11_20])
	giver21_30  = SampleGiver.objects.extra(where=[from_21_30])
	giver31_40  = SampleGiver.objects.extra(where=[from_31_40])
	giver41more = SampleGiver.objects.extra(where=[from_41_end])
	giverOther  = SampleGiver.objects.filter(age__isnull=True)
	
	ratio0_10   = getRatio(giver0_10,   allGiver, giverOther)
	ratio11_20  = getRatio(giver11_20,  allGiver, giverOther)
	ratio21_30  = getRatio(giver21_30,  allGiver, giverOther)
	ratio31_40  = getRatio(giver31_40,  allGiver, giverOther)
	ratio41more = getRatio(giver41more, allGiver, giverOther)
	ratioGiverOther = getRatio(giverOther, allGiver)
	stringToReturn = [
		[str(_(u"De 0 à 10 ans ("))+str(len(giver0_10))+")",ratio0_10], 
		[str(_(u"De 11 à 20 ans ("))+str(len(giver11_20))+")",ratio11_20], 
		[str(_(u"De 21 à 30 ans ("))+str(len(giver21_30))+")",ratio21_30], 
		[str(_(u"De 31 à 40 ans ("))+str(len(giver31_40))+")",ratio31_40],
		[str(_(u"De 41 ans & plus ("))+str(len(giver41more))+")",ratio41more] 
		#["Sans renseignements ("+str(len(giverOther))+")",ratioGiverOther]
		]
	return stringToReturn
	

###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__ == "__main__" :

	print 'Test in local\n.'
