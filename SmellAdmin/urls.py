#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('SmellAdmin.views',#main path
                       #url(r'^main/$', 'adminView'),
                       url(r'^$', 'adminView'),
                       url(r'^thanks/$', 'adminThankView'),
)