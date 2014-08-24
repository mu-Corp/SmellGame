from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^home/$', 'SmellGuess.views.home'),
                       url(r'^identification/$', 'SmellGuess.views.identification'),
                       url(r'^game/$', 'SmellGuess.views.game'),
                       #url(r'^URL_name/$', 'AppName.views.FunctionName'),
)