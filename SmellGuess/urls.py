#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url



urlpatterns = patterns('SmellGuess.views',#main path
                       url(r'^home/$', 'homeView'),
                       url(r'^registration/$', 'registrationView'),
                       url(r'^game/$', 'gameView'),
                       #url(r'^game/(?P<user>\d{0})/$', 'game'),
                       #url(r'^URL_name/$', 'AppName.views.FunctionName'),
)