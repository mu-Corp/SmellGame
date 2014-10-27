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
'''To delete !!!
class Administrator(models.Model):
	#Primary key (not in form)
	id                = models.AutoField(primary_key=True)
	
	#Fields visibles in form:
	username               = models.CharField(max_length=20, default='F', null=True)
	password               = models.CharField(max_length=20, default='F', null=True)
	
	#Hidden fields:
	date_registration = models.DateTimeField(auto_now_add=True, null=True)
'''
###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__ == "__main__" :

	print 'Test in local\n.'