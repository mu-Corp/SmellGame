#-*- coding: utf-8 -*-

################################################################
#######################    LIBRARIES    ########################
################################################################

from django import forms

################################################################
########################    CLASSES    #########################
################################################################

class ConnexionForm(forms.Form):
	"""Definition of the form for identification for admin app

	Parameters
	----------
	forms.ModelForm : ???
		???

	Examples
	--------

	See also
	--------
	- SdZ tuto: http://fr.openclassrooms.com/informatique/cours/developpez-votre-site-web-avec-le-framework-django/les-utilisateurs-2

	"""
	
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
	
	
	