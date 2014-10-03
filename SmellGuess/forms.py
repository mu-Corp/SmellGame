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
    """Definition of smeller form from Smeller Class.

    Enable to determine which of attribut of Smeller will be available in form.

    Parameters
    ----------
    forms.ModelForm : ???
        ???

    Examples
    --------

    See also
    --------
    - Official doc: https://docs.djangoproject.com/fr/1.6/topics/forms/modelforms/
    - Image for radio value: http://stackoverflow.com/questions/4708700/how-do-i-make-a-radioselect-have-a-image-as-radio-value
    - 

    Notes
    -----
    TODO: Image for radio value for sex ???

    """
    
    class Meta:
        model = Smeller  # Form with fields of Smeller class
        exclude = ('samples',) # Exclude field "sample" in the form
        fields = ('age', 'sex')
        
        labels = {
            'age': 'Âge ',
            'sex': 'Sexe '
        }





from django.forms import ModelForm, RadioSelect
from django.forms.widgets import HiddenInput

class SmellerModelForm2(forms.ModelForm):
    class Meta:
        model = Smeller  # Form with fields of Smeller class
        exclude = ('samples',) # Exclude field "sample" in the form
        
        
        widgets = {
            'sex': RadioSelect(attrs=None),
        }
        
        
        #Change the param of the text face to the field
        labels = {
            'sex': 'coucou',
        }
        
    
        
        