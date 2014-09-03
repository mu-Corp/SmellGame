#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django.db import models
import random #random number for listToSmell

################################################################
#######################    FUNCTIONS    ########################
################################################################

def scoring(listToSmell):
	# function of scoring. 
	
	return

'''
def isCorrect(spl, odor): 
	# Make the verification between answer and correct odor.
	# Increment the sample/refSample corresponding object
	#for elt in odor : --> if odor can be a list of proposition (see in drag&drop return possibilities)
	if spl == odor : 
		spl.nb_outed   = spl.nb_outed + 1
		spl.nb_correct = spl.nb_correct + 1
		return 1 #possibility to change by a ratio of correct answer
	else : 
		spl.nb_outed   = spl.nb_outed + 1
		#spl.nb_correct = 0
		return 0 #possibility to change by a ratio of correct answer
'''

def getOdorToGuess():
	# Return a list of tube (identify by number) to guess
	# 3 of reference odor (vegetable , ...) and 3 of samples
	listToSmell = []
	listRef     = []
	listNotRef  = []
	for elt in Sample.objects.all():
		if elt.refOdor == True :
			listRef.append(elt.id)
		else :
			listNotRef.append(elt.id)
	print 'listNotRef', len(listNotRef)
	print 'listRef',    len(listRef)
	
	# Part 1 : RefOdor
	i=0
	while i<3 :
		nthToAdd =random.randint(0,len(listRef)-1) 
		print nthToAdd
		if listRef[nthToAdd] not in listToSmell :
			listToSmell.append(listRef[nthToAdd])
			i += 1
			
	# Part 2 : Sample
	i=0
	while i<3 :
		nthToAdd =random.randint(0,len(listNotRef)-1) 
		print nthToAdd
		if listNotRef[nthToAdd] not in listToSmell :
			listToSmell.append(listNotRef[nthToAdd])
			i += 1
	return listToSmell

################################################################
########################    CLASSES    #########################
################################################################

class Smeller(models.Model):
	id                = models.AutoField(primary_key=True)
	name              = models.CharField(max_length=42, default='')
	email             = models.CharField(max_length=100, default='')
	SEX_CHOICE        = (('M', 'Male'),('F', 'Female'),)
	sex               = models.CharField(max_length=1, choices=SEX_CHOICE,default='F')
	age               = models.PositiveSmallIntegerField(default=18)
	date_registration = models.DateTimeField(auto_now_add=True)
	samples = models.ManyToManyField('Sample', through='Guess')
	
################################################################
	
class Sample(models.Model):
	id   = models.AutoField(primary_key=True)
	name = models.CharField(max_length=42)
	nb_outed   = models.PositiveSmallIntegerField(default=0)
	nb_guesses = models.PositiveSmallIntegerField(default=0)
	refOdor = models.BooleanField(default=False)

################################################################

class Guess(models.Model): 
	smeller   = models.ForeignKey('Smeller')
	sample    = models.ForeignKey('Sample')
	intensity = models.PositiveSmallIntegerField()
	odor      = models.PositiveSmallIntegerField()
	perfumes  = models.ManyToManyField('Perfume')
	'''correct   = isCorrect(sample, odor) #add a verification at the sending of answer'''

################################################################

class Perfume(models.Model):
	id   = models.AutoField(primary_key=True)
	name = models.CharField(max_length=42)
	path = models.CharField(max_length=42)

	

###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__ == "__main__" :

	print 'Test in local\n.'
	
