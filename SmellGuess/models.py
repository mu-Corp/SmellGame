#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django.db import models


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

################################################################

class Guess(models.Model): 
	smeller   = models.ForeignKey('Smeller')
	sample    = models.ForeignKey('Sample')
	intensity = models.PositiveSmallIntegerField()
	odor      = models.PositiveSmallIntegerField()
	perfumes  = models.ManyToManyField('Perfume')

################################################################

class Perfume(models.Model):
	id   = models.AutoField(primary_key=True)
	name = models.CharField(max_length=42)

	
################################################################
#######################    FUNCTIONS    ########################
################################################################

###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__ == "__main__" :

	print 'Test in local\n.'
