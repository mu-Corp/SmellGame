#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('SmellGuess.views',#main path
                       url(r'^home/$', 'homeView'),
                       url(r'^registration/$', 'registrationView'),
                       url(r'^game/$', 'gameView'),
                       url(r'^result/$', 'resultView'),
                       url(r'^error/$', 'errorview'),
                       #url(r'^game/(?P<user>\d{0})/$', 'game'),
                       #url(r'^URL_name/$', 'AppName.views.FunctionName'),
                       url(r'^admin/', include(admin.site.urls)),
)