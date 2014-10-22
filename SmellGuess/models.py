#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django.db import models
from django.utils.translation import ugettext_lazy as _

################################################################
#######################    FUNCTIONS    ########################
################################################################

	
################################################################
########################    CLASSES    #########################
################################################################

class Sample(models.Model):
	id          = models.AutoField(primary_key=True)
	name        = models.CharField(max_length=42, null=True)
	sampleGiver = models.ForeignKey('SmellGift.SampleGiver', null=True, default=None)
	available   = models.BooleanField(default=False)

################################################################
class Smeller(models.Model):
	
	#Primary key (not in form)
	id                = models.AutoField(primary_key=True)
	
	#Fields visibles in form:
	SEX_CHOICE        = (('M', _(u'Homme')),('F', _(u'Femme')),)
	sex               = models.CharField(max_length=1, choices=SEX_CHOICE,default='F', null=True)
	age               = models.PositiveSmallIntegerField(default=18, null=True)
	
	#Hidden fields:
	date_registration = models.DateTimeField(auto_now_add=True, null=True)


################################################################

class Guess(models.Model): 
	id         = models.AutoField(primary_key=True)
	smeller    = models.ForeignKey('Smeller', null=True)
	sample     = models.ForeignKey('Sample', null=True)
	intensity  = models.PositiveSmallIntegerField(default=0, null=True)
	humor      = models.ForeignKey('Humor', null=True)
	note       = models.ForeignKey('Note', null=True)
	image      = models.ForeignKey('Image', null=True)
	feeling    = models.PositiveSmallIntegerField(default=0, null=True)
	name       = models.CharField(max_length=42, null=True)
	
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
	
