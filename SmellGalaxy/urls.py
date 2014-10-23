#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('SmellGalaxy.views',
                       #url(r'^URL_name/$', 'AppName.views.FunctionName'),
					   url(r'^$', 'Graphes'), #Demo highchart
)
