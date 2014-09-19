#-*- coding: utf-8 -*-
from django.test import TestCase

# Create your tests here.

from random import sample



azer = sample([1, 2, 3, 4, 5],  3)

print azer
azer2 = azer.remove(azer[0])
print azer
print azer2
print type(azer)



