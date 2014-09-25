#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django.db import models
import random #random number for listToSmell
#from djangotoolbox.fields import ListField

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
	#for elt in odor :
	if spl == odor : 
		spl.nb_outed   = spl.nb_outed + 1
		spl.nb_correct = spl.nb_correct + 1
		return 1 #possibility to change by a ratio of correct answer
	else : 
		spl.nb_outed   = spl.nb_outed + 1
		#spl.nb_correct = 0
		return 0 #possibility to change by a ratio of correct answer
'''

def getOdorToGuess(theSmeller):
		listToSmell = []
		listRef     = []
		listNotRef  = []
		for elt in Sample.objects.all():
			if elt.refOdor == True :
				listRef.append(elt)
			else :
				listNotRef.append(elt)
		print 'listNotRef', len(listNotRef)
		print 'listRef',    len(listRef)
		
		# Part 1 : RefOdor
		i=0
		if len(listRef)-1 >=3:
			max = len(listRef)-1; #print "m1", max
			while i<3 :
				nthToAdd =random.randint(0,max) 
				if listRef[nthToAdd] not in listToSmell :
					listToSmell.append(listRef[nthToAdd])
					i += 1
		else :
			print 'error : listRef'
			return False
				
		# Part 2 : Sample odor
		i=0
		if len(listNotRef)-1 >=3:
			max = len(listNotRef)-1; #print "m2",max
			while i<3 :
				nthToAdd =random.randint(0,max) 
				if listNotRef[nthToAdd] not in listToSmell :
					listToSmell.append(listNotRef[nthToAdd])
					i += 1
		else :
			print 'error : listNotRef'
			return False
		print 'listToSmell : ', listToSmell
		for elt in listToSmell : 
			print 'newGuessing = Guess(sample=Guess.sample('+str(elt.id)+'), smeller='+str(theSmeller.id)+')'
			newGuessing = Guess(smeller=theSmeller, sample=elt)
			newGuessing.save()
		return
	
################################################################
########################    CLASSES    #########################
################################################################

class Sample(models.Model):
	id   = models.AutoField(primary_key=True)
	name = models.CharField(max_length=42)

################################################################
class Smeller(models.Model):
	
	#Primary key (not in form)
	id                = models.AutoField(primary_key=True)
	
	#Fields visibles in form:
	SEX_CHOICE        = (('M', 'Male'),('F', 'Female'),)
	sex               = models.CharField(max_length=1, choices=SEX_CHOICE,default='F')
	age               = models.PositiveSmallIntegerField(default=18)
	
	#Hidden fields:
	date_registration = models.DateTimeField(auto_now_add=True)


################################################################

class Guess(models.Model): 
	id         = models.AutoField(primary_key=True)
	smeller    = models.ForeignKey('Smeller', null=True)
	sample     = models.ForeignKey('Sample', null=True)
	intensity  = models.PositiveSmallIntegerField(default=0)
	humor      = models.ForeignKey('Humor', null=True)
	note       = models.ForeignKey('Note', null=True)
	image      = models.ForeignKey('Image', null=True)
	feeling    = models.PositiveSmallIntegerField(default=0)
	name       = models.CharField(max_length=42)
	
###############################################################

class Humor(models.Model):
	id    = models.AutoField(primary_key=True)
	name  = models.CharField(max_length=42)
	color = models.CharField(max_length=42)

###############################################################

class Note(models.Model):
	id    = models.AutoField(primary_key=True)
	name  = models.CharField(max_length=42)
	color = models.CharField(max_length=42)

###############################################################

class Image(models.Model):
	id    = models.AutoField(primary_key=True)
	name  = models.CharField(max_length=42)
	pathImage = models.CharField(max_length=42)

###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__ == "__main__" :

	print 'Test in local\n.'
	
