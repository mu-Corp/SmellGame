#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django import forms
from models import Smeller, Guess

################################################################
########################    CLASSES    #########################
################################################################

class SmellerModelForm(forms.ModelForm):
    class Meta:
        model = Smeller  # Form with fields of Smeller class
        exclude = ('samples',) # Exclude field "sample" in the form

class GuessModelForm(forms.ModelForm):
    class Meta:
        model = Guess # Form with fields of Guess class
        widgets = {'perfumes': forms.HiddenInput()}  # Field "perfumes" = id perfumes list
        exclude = ('smeller','sample',) # Exclude fields "smeller" and "sample" in the form
