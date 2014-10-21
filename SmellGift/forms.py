#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django import forms
from widgets import SelectTimeWidget, RangeWidget
from models import SampleGiver, Food

################################################################
########################    CLASSES    #########################
################################################################

class SampleGiverForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(SampleGiverForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = False
		self.fields['foodRecentlyEaten'].required = False
		
	class Meta:
		model = SampleGiver  # Form with fields of Smeller class
		#exclude = ('samples',) # Exclude field "sample" in the form
		
		fields = ('age','sex','smoker','diet','foodRecentlyEaten','deodorant','email','testDuration','activity','intensity','feeling')
		
		widgets = { 'sex': forms.widgets.RadioSelect(),
			    'smoker': forms.widgets.RadioSelect(choices=[(1, 'Oui'), (0, 'Non')]),
			    'foodRecentlyEaten': forms.widgets.CheckboxSelectMultiple(),
			    'deodorant': forms.widgets.RadioSelect(choices=[(1, 'Oui'), (0, 'Non')]),
			    'diet': forms.widgets.RadioSelect(),
			    'testDuration': SelectTimeWidget(),
			    'activity': forms.widgets.RadioSelect(),
			    'intensity': RangeWidget(LabelBefore='Faible', LabelAfter='Forte'),
			    'feeling': RangeWidget(LabelBefore=u'Agréable', LabelAfter=u'Désagréable')}
		
		labels = { 'age': 'Âge ',
			   'sex': 'Sexe ',
			   'smoker': 'Fumeur ',
			   'diet': 'Régime ',
			   'foodRecentlyEaten': 'Récemment consommé ',
			   'deodorant': 'Déodorant ',
			   'email': 'E-mail ',
			   'testDuration': 'Durée du test ',
			   'activity': 'Activité suivie ',
			   'intensity': '',
			   'feeling': ''}
        
        