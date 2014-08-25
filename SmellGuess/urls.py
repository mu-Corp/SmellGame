#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url



urlpatterns = patterns('SmellGuess.views',#main path
                       url(r'^home/$', 'home'),
                       url(r'^identification/$', 'enter'),
                       url(r'^game/$', 'game'),
                       #url(r'^URL_name/$', 'AppName.views.FunctionName'),
)