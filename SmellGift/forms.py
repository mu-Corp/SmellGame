#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django import forms
from models import SampleGiver

################################################################
########################    CLASSES    #########################
################################################################

class SampleGiverForm(forms.ModelForm):
	class Meta:
		model = SampleGiver  # Form with fields of Smeller class
		#exclude = ('samples',) # Exclude field "sample" in the form
		#fields = ('age', 'sex')

		labels = { 'age': 'Âge ',
			   'sex': 'Sexe ' }
        
        