#-*- coding: utf-8 -*-
from django.test import TestCase

# Create your tests here.

from random import sample

azer = [1, 2, None, 3]
print azer
print type(azer[0])
print type(azer[2])

if isinstance(azer[0], int):
    print 'helo' + str(type(azer[0]))
else: 
    print 'noo'