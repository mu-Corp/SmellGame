#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django import forms
from models import SampleGiver, Food

################################################################
########################    CLASSES    #########################
################################################################

class SampleGiverForm(forms.ModelForm):
	#def __init__(self, *args, **kwargs):
		#super(SampleGiverForm, self).__init__(*args, **kwargs)
		#self.fields['foodRecentlyEaten'].widget = forms.CheckboxSelectMultiple()
	
	class Meta:
		model = SampleGiver  # Form with fields of Smeller class
		#exclude = ('samples',) # Exclude field "sample" in the form
		
		fields = ('age','sex','smoker','diet','foodRecentlyEaten','deodorant','email','testDuration','activity','intensity','feeling')
		
		#fields[5].widget = forms.CheckboxSelectMultiple()
		widgets = { 'sex': forms.widgets.RadioSelect(),
			    'foodRecentlyEaten': forms.widgets.CheckboxSelectMultiple(),
			    'diet': forms.widgets.RadioSelect(),
			    'activity': forms.widgets.RadioSelect() }

		labels = { 'age': 'Âge ',
			   'sex': 'Sexe ',
			   'smoker': 'Fumeur ',
			   'diet': 'Régime ',
			   'foodRecentlyEaten': 'Récemment consommé ',
			   'deodorant': 'Déodorant ',
			   'email': 'E-mail ',
			   'testDuration': 'Durée du test ',
			   'activity': 'Activité suivie '}
        
        