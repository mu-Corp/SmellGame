#-*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse





def home(request):
    text = """<h1>Bienvenue sur SmellGame !</h1>
              <p>Ceci est la page d'accueil. Il va falloir créer un template adéquate pour cette page (Nathan). !</p>"""
              
    return HttpResponse(text)



def identification(request):
    text = """<h1>Vous êtes sur la page d'identification !</h1>
              <p>Il va falloir créer un template adéquate pour cette page (Nathan).</p>"""
              
    return HttpResponse(text)



def game(request):
    text = """<h1>Vous êtes sur la page du jeu !</h1>
              <p>Il va falloir créer un template adéquate pour cette page (Nathan).</p>"""
              
    return HttpResponse(text)