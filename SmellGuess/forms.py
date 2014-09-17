#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django import forms
from models import Smeller

################################################################
########################    CLASSES    #########################
################################################################

class SmellerModelForm(forms.ModelForm):
    class Meta:
        model = Smeller  # Form with fields of Smeller class
        exclude = ('samples',) # Exclude field "sample" in the form