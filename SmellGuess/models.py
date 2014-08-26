#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django.db import models

################################################################
########################    CLASSES    #########################
################################################################

# TO DO: Change the fields (Lucas)
class Smeller(models.Model):
    name = models.CharField(max_length=42)
    email = models.CharField(max_length=100)
    SEX_CHOICE = (('M', 'Male'),('F', 'Female'),)
    sex = models.CharField(max_length=1, choices=SEX_CHOICE, default='F')
    age = models.PositiveSmallIntegerField()
    date_registration = models.DateTimeField()
    
################################################################

# TO DO: Change the fields (Flo) 
class Sample(models.Model):
    intensity = models.CharField(max_length=42)
    deo = models.BooleanField()
    deo_type = models.CharField(max_length=42)
    food_type = models.CharField(max_length=42)
    smeller = models.ForeignKey('Smeller')


    
################################################################
#######################    FUNCTIONS    ########################
################################################################



###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__=="__main__": 
    
    print 'Test in local\n.'
    
