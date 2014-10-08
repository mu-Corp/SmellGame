#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('SmellGift.views',#main path
                       url(r'^$', 'giftView'),
                       url(r'^thanks/$', 'thanksView'),
)