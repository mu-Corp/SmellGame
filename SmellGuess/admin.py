#-*- coding: utf-8 -*-
from django.contrib import admin
from SmellGuess.models import *
# Register your models here.


admin.site.register(Sample)
admin.site.register(Smeller)
admin.site.register(Guess)