#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django.db import models

################################################################
########################    CLASSES    #########################
################################################################

# TO DO: Change the fields (Lucas)
'''
class Smeller(models.Model):
    id_smeller = models.CharField(max_length=100)
    name_smeller = models.CharField(max_length=42)

#sex_smeller = models.Charfield(max_length=1)#M/F
	MALE = 'M'
	FEMALE = 'F'
	SEX_CHOICE = ((MALE, 'Male'),(FEMALE, 'Female'),)
	sex_smeller = models.Charfield(max_lengt=1,choices=SEX_CHOICE,default=MALE)

age_smeller = models.PositiveSmallIntegerField()
'''

################################################################

'''  
# TO DO: Change the fields (Flo)
class Sample(models.Model):
    name = models.CharField(max_length=42)
    intensity = models.CharField(max_length=42)
	sex = models.CharField(max_length=42)
	old = models.PositiveSmallIntegerField()
	deo = models.BooleanField()
	deo_type = models.CharField(max_length=42)
	food_type = models.CharField(max_length=42)
'''
    
################################################################
#######################    FUNCTIONS    ########################
################################################################



###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__=="__main__": 
    
    print 'Test in local\n.'
    
