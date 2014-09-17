#-*- coding: utf-8 -*-

from SmellGuess.models import *

if len(Sample.objects.all()) == 0 :
	# Creating samples
	Sample(name='d1').save()
	Sample(name='d2').save()
	Sample(name='d3').save()
	Sample(name='d4').save()
	Sample(name='d5').save()
	Sample(name='d6').save()
	Sample(name='d7').save()
	Sample(name='d8').save()
	Sample(name='d9').save()
	Sample(name='d9').save()
	print "Samples created"
else : 
	print "Please remove db.sqlite3 and execute 'python manage.py syncb' before !"
	exit()


if len(Humor.objects.all()) == 0 :
	# Creating humors
	Humor(name="AFFECTION",  color="rgb(150,200,80)").save()
	Humor(name="ANXIÉTÉ",    color="rgb(200,255,10)").save()
	Humor(name="BONHEUR",    color="rgb(20,40,80)").save()
	Humor(name="COLÈRE",     color="rgb(27,178,130)").save()
	Humor(name="DÉPRESSION", color="rgb(100,200,255)").save()
	Humor(name="DOUCEUR",    color="rgb(200,20,20)").save()
	Humor(name="EXCITATION", color="rgb(100,100,200)").save()
	Humor(name="FOLIE",      color="rgb(200,30,0)").save()
	Humor(name="IRRITATION", color="rgb(0,10,200)").save()
	Humor(name="NERVOSITÉ",  color="rgb(135,220,230)").save()
	Humor(name="PEUR",       color="rgb(230,135,220)").save()
	Humor(name="RAGE",       color="rgb(0,120,120)").save()
	Humor(name="TRISTESSE",  color="rgb(240,120,12)").save()
	print "Humors created"
else : 
	print "Please remove db.sqlite3 and execute 'python manage.py syncb' before !"
	exit()


if len(Note.objects.all()) == 0 :
	# Creating notes
	Note(name="ANIMALE",  color="rgb(20,80,128)").save()
	Note(name="CHIMIQUE", color="rgb(50,154,12)").save()
	Note(name="ÉPICÉE",   color="rgb(221,232,34)").save()
	Note(name="FRUITÉE",  color="rgb(200,81,67)").save()
	Note(name="GRASSE",   color="rgb(135,54,150)").save()
	Note(name="VÉGÉTALE", color="rgb(170,123,255)").save()
	print "Notes created"
else : 
	print "Please remove db.sqlite3 and execute 'python manage.py syncb' before !"
	exit()


if len(CommonName.objects.all()) == 0 :
	# Creating common names
	CommonName(name="POISSON",             pathImage="images/CommonName/poisson.png").save()
	CommonName(name="CHIEN MOUILLÉ",       pathImage="images/CommonName/chienMouille.png").save()
	CommonName(name="BOUC / CHÈVRE",       pathImage="images/CommonName/boucChevre.png").save()
	CommonName(name="SANGLIER",            pathImage="images/CommonName/sanglier.png").save()
	CommonName(name="BOUILLON DE POULET",  pathImage="images/CommonName/bouillonDePoulet.png").save()
	CommonName(name="FROMAGE",             pathImage="images/CommonName/fromage.png").save()
	CommonName(name="BEURRE RANCE",        pathImage="images/CommonName/beurreRance.png").save()
	CommonName(name="RAISIN",              pathImage="images/CommonName/raisin.png").save()
	CommonName(name="FRUIT DE LA PASSION", pathImage="images/CommonName/fruitDeLaPassion.png").save()
	CommonName(name="ONION",               pathImage="images/CommonName/onion.png").save()
	CommonName(name="AIL",                 pathImage="images/CommonName/ail.png").save()
	CommonName(name="CHOUX",               pathImage="images/CommonName/choux.png").save()
	CommonName(name="ASPERGE",             pathImage="images/CommonName/asperge.png").save()
	CommonName(name="MENTHE",              pathImage="images/CommonName/menthe.png").save()
	CommonName(name="PIMENT",              pathImage="images/CommonName/piment.png").save()
	CommonName(name="CUMIN",               pathImage="images/CommonName/cumin.png").save()
	CommonName(name="CURCUMA",             pathImage="images/CommonName/curcuma.png").save()
	CommonName(name="VINEGRE",             pathImage="images/CommonName/vinegre.png").save()
	CommonName(name="ALCOOL",              pathImage="images/CommonName/alcool.png").save()
	CommonName(name="ESSENCE",             pathImage="images/CommonName/essence.png").save()
	print "Common names created"
else : 
	print "Please remove db.sqlite3 and execute 'python manage.py syncb' before !"
	exit()