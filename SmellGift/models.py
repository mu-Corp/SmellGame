#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django.db import models

################################################################
#######################    FUNCTIONS    ########################
################################################################

	
################################################################
########################    CLASSES    #########################
################################################################

class SampleGiver(models.Model):
	#Primary key (not in form)
	id                = models.AutoField(primary_key=True)
	
	#Choices:
	SEX_CHOICE        = (('M', 'Homme'),('F', 'Femme'),)
	DIET_CHOICE       = (('HP', 'Hyper protéiné'),
		             ('VR', 'Végétarien'),
		             ('VL', 'Végétalien'),
		             ('N', 'Aucun'),)
	ACTIVITY_CHOICE   = (('SP', 'Sport'),
		             ('SO', 'Sommeil'),
		             ('T', 'Travail'),
		             ('N', 'Aucune'),
		             ('A', 'Autre'),)
	
	#Fields visibles in form:
	age               = models.PositiveSmallIntegerField(default=18)
	sex               = models.CharField(max_length=1, choices=SEX_CHOICE,default='F')
	smoker            = models.BooleanField(default=False)
	diet              = models.CharField(max_length=2, choices=DIET_CHOICE,default='N')
	foodRecentlyEaten = models.ManyToManyField('Food')
	deodorant         = models.BooleanField(default=True)
	email             = models.EmailField(max_length=254)
	testDuration      = models.CharField(max_length=15)
	activity          = models.CharField(max_length=2, choices=ACTIVITY_CHOICE,default='N')
	intensity         = models.PositiveSmallIntegerField(default=0)
	feeling           = models.PositiveSmallIntegerField(default=0)
	
	#Hidden fields:
	date_registration = models.DateTimeField(auto_now_add=True)

###############################################################	

class Food(models.Model):
	id   = models.AutoField(primary_key=True)
	name = models.CharField(max_length=42)
	
	def __unicode__(self): return self.name


###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__ == "__main__" :

	print 'Test in local\n.'