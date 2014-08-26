#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django import forms
from models import Smeller

################################################################
########################    CLASSES    #########################
################################################################

class DataSmellerForm(forms.Form):
    username = forms.CharField(max_length=100)
    sex = forms.CharField(max_length=100)
    sexe = forms.CheckboxInput()

class SmellerModelForm(forms.ModelForm):
    class Meta:
        model = Smeller
