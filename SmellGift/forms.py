#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django import forms
from django.utils.translation import ugettext_lazy as _
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
		
		fields = ('age','sex','smoker','diet','foodRecentlyEaten','deodorant','email','testDuration','activity','intensity','feeling')
		
		widgets = { 'sex': forms.widgets.RadioSelect(),
			    'smoker': forms.widgets.RadioSelect(choices=[(1, _(u'Oui')), (0, _(u'Non'))]),
			    'foodRecentlyEaten': forms.widgets.CheckboxSelectMultiple(),
			    'deodorant': forms.widgets.RadioSelect(choices=[(1, _(u'Oui')), (0, _(u'Non'))]),
			    'diet': forms.widgets.RadioSelect(),
			    'testDuration': SelectTimeWidget(),
			    'activity': forms.widgets.RadioSelect(),
			    'intensity': RangeWidget(LabelBefore=_(u'Faible'), LabelAfter=_(u'Forte')),
			    'feeling': RangeWidget(LabelBefore=_(u'Agréable'), LabelAfter=_(u'Désagréable'))}
		
		labels = { 'age': _(u'Âge '),
			   'sex': _(u'Sexe '),
			   'smoker': _(u'Fumeur '),
			   'diet': _(u'Régime '),
			   'foodRecentlyEaten': _(u'Récemment consommé '),
			   'deodorant': _(u'Déodorant '),
			   'email': _(u'E-mail '),
			   'testDuration': _(u'Durée du test '),
			   'activity': _(u'Activité suivie '),
			   'intensity': '',
			   'feeling': ''}
        
        