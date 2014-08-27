#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django.db    import  models


################################################################
########################    CLASSES    #########################
################################################################

# TO DO: Change the fields (Lucas)
class Smeller(models.Model):
	name    = models.CharField(max_length=42)
	email   = models.CharField(max_length=100)
	#smeller = models.BooleanField()
	#sampler = models.BooleanField()
	SEX_CHOICE = (('M', 'Male'),('F', 'Female'),)
	sex     = models.CharField(max_length=1, choices=SEX_CHOICE,default='F')
	age     = models.PositiveSmallIntegerField()
	#deo_type     = models.CharField(max_length=42)
	#food_type    = models.CharField(max_length=42)
	date_registration = models.DateTimeField(auto_now_add=True)
	id_person = models.AutoField(primary_key=True)
	
	

################################################################

# TO DO: Change the fields (Flo)
class Sample(models.Model):
	#name_sampler = models.ForeignKey(Person, related_name='+')
	name_smeller = models.ForeignKey(Smeller, related_name='+')
	intensity    = models.CharField(max_length=42)
	id_sample    = models.AutoField(primary_key=True)
	date_registration = models.DateTimeField()
	

    
################################################################
#######################    FUNCTIONS    ########################
################################################################

###############################################################
####################    LOCAL EXECUTION    ####################
###############################################################
if __name__ == "__main__" :

	print 'Test in local\n.'



