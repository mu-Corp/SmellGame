#-*- coding: utf-8 -*-
from django.test import TestCase

# Create your tests here.

dict_SliceOfAge["giver0_10"]   = SampleGiver.objects.extra(where=[getFromTo(crit, 0, 10)])
dict_SliceOfAge["giver11_20"]  = SampleGiver.objects.extra(where=[getFromTo(crit, 11, 20)])
dict_SliceOfAge["giver21_30"]  = SampleGiver.objects.extra(where=[getFromTo(crit, 21, 30)])


print (doMoyFeelingForAllGivers(dict_SliceOfAge["giver0_10"]))
print (doMoyFeelingForAllGivers(dict_SliceOfAge["giver11_20"]))
print (doMoyFeelingForAllGivers(dict_SliceOfAge["giver21_30"]))

