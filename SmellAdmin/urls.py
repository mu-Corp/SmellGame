#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('SmellAdmin.views',#main path
                       url(r'^$', 'adminView', name='connexion'),
                       url(r'^thanks/$', 'adminThankView'),
                       url(r'^deco/$', 'decoView'),
)