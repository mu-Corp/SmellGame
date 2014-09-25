#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django.db import models
import random

################################################################
#######################    FUNCTIONS    ########################
################################################################

	
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
	
