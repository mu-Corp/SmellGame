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
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
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
    
