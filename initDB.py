#-*- coding: utf-8 -*-

from SmellGuess.models import *

if len(Sample.objects.all()) == 0 :
	# Creating samples
	for i in range(50) :
		Sample(name='d'+str(i)).save()
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


if len(Image.objects.all()) == 0 :
	# Creating common names
	Image(name="POISSON",             pathImage="images/Image/poisson.png").save()
	Image(name="CHIEN MOUILLÉ",       pathImage="images/Image/chienMouille.png").save()
	Image(name="BOUC / CHÈVRE",       pathImage="images/Image/boucChevre.png").save()
	Image(name="SANGLIER",            pathImage="images/Image/sanglier.png").save()
	Image(name="BOUILLON DE POULET",  pathImage="images/Image/bouillonDePoulet.png").save()
	Image(name="FROMAGE",             pathImage="images/Image/fromage.png").save()
	Image(name="BEURRE RANCE",        pathImage="images/Image/beurreRance.png").save()
	Image(name="RAISIN",              pathImage="images/Image/raisin.png").save()
	Image(name="FRUIT DE LA PASSION", pathImage="images/Image/fruitDeLaPassion.png").save()
	Image(name="OIGNON",              pathImage="images/Image/oignon.png").save()
	Image(name="AIL",                 pathImage="images/Image/ail.png").save()
	Image(name="CHOUX",               pathImage="images/Image/choux.png").save()
	Image(name="ASPERGE",             pathImage="images/Image/asperge.png").save()
	Image(name="MENTHE",              pathImage="images/Image/menthe.png").save()
	Image(name="PIMENT",              pathImage="images/Image/piment.png").save()
	Image(name="CUMIN",               pathImage="images/Image/cumin.png").save()
	Image(name="VINAIGRE",            pathImage="images/Image/vinaigre.png").save()
	Image(name="ALCOOL",              pathImage="images/Image/alcool.png").save()
	Image(name="ESSENCE",             pathImage="images/Image/essence.png").save()
	print "Images created"
else : 
	print "Please remove db.sqlite3 and execute 'python manage.py syncb' before !"
	exit()