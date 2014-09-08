#-*- coding: utf-8 -*-

#creer les bases de données selon les objet présennts
#python manage.py syncdb

#Lance un interpreteur local pour tester les objets
#python manage.py shell

#class Smeller(name, email, smeller, sampler, SEX_CHOICE, age) 
	#pas a definir : #deo_type, #food_type, date_registration, id_Sample

#import pour le test 
from SmellGuess.models import *
#from models import *

if len(Sample.objects.all()) == 0 :
	# Creation de Sample
	spl_1  = Sample(name='banane',refOdor = True )
	spl_2  = Sample(name='pomme',refOdor = True )
	spl_3  = Sample(name='kiwi',refOdor = True )
	spl_4  = Sample(name='fraise',refOdor = True )
	spl_5  = Sample(name='poivre',refOdor = True )
	spl_6  = Sample(name='curry',refOdor = True )
	spl_7  = Sample(name='endive',refOdor = True )
	spl_8  = Sample(name='d1',refOdor = False)
	spl_9  = Sample(name='d2',refOdor = False)
	spl_10 = Sample(name='d3',refOdor = False)
	spl_11 = Sample(name='d4',refOdor = False)
	spl_12 = Sample(name='d5',refOdor = False)
	spl_13 = Sample(name='d6',refOdor = False)
	spl_14 = Sample(name='d7',refOdor = False)
	spl_15 = Sample(name='d8',refOdor = False)
	spl_16 = Sample(name='d9',refOdor = False)
	spl_17 = Sample(name='d9',refOdor = False)

	# Enregistrement des samples
	spl_1.save();spl_2.save();spl_3.save();spl_4.save();spl_5.save()
	spl_6.save();spl_7.save();spl_8.save();spl_9.save();spl_10.save()
	spl_11.save();spl_12.save();spl_13.save();spl_14.save();spl_15.save();
	spl_16.save();spl_17.save();
	print "Creation des samples"

# Create/save Smeller
if len(Smeller.objects.all()) == 0 :
	# Create Smeller
	indA = Smeller(name=u"individu A", email=u"indA@email.com", sex='M', age=10) 
	indB = Smeller(name=u"individu B", email=u"indB@email.com", sex='M', age=29) 
	indC = Smeller(name=u"individu C", email=u"indC@email.com", sex='M', age=33) 
	indD = Smeller(name=u"individu D", email=u"indD@email.com", sex='M', age=18) 
	indE = Smeller(name=u"individu E", email=u"indE@email.com", sex='M', age=51) 
	indF = Smeller(name=u"individu F", email=u"indF@email.com", sex='M', age=37) 

	# save Smeller in db
	indA.save();indB.save();indC.save();
	indD.save();indE.save();indF.save();
	print "Creation des individus (smellers)."
	
#creation de la liste de guess
for elt in Smeller.objects.all():
	print elt , elt.id
	if len(Guess.objects.filter(smeller = elt.id)) == 0:
		getOdorToGuess(elt)

# Create Perfume
perfume1= Perfume(name=u"banane", path=u"images/Perfume/banana.png")
perfume2= Perfume(name=u"foot", path=u"images/Perfume/foot.png")
perfume3= Perfume(name=u"forest", path=u"images/Perfume/forest.png")
perfume4= Perfume(name=u"grass", path=u"images/Perfume/grass.png")

perfume1.save();perfume2.save();perfume3.save();perfume4.save();
