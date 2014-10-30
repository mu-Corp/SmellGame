#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('SmellGalaxy.views',
                       #url(r'^URL_name/$', 'AppName.views.FunctionName'),
			url(r'^$', 'graphesView'), #Demo highchart
            url(r'^graphes/$', 'paraGraphesView'), #Demo highchart
)
