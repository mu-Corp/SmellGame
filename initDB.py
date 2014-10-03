#-*- coding: utf-8 -*-

from SmellGuess.models import *

if len(Sample.objects.all()) == 0 :
	# Creating samples
	for i in range(1,101) :
		Sample(name="S"+str(i)).save()
	for i in range(1,11) :
		Sample(name="PB"+str(i)).save()
		Sample(name="PB"+str(i)+"'").save()
	for i in range(1,27) :
		Sample(name="CS"+str(i)).save()
	print "Samples created"
else : 
	print "Please remove db.sqlite3 and execute 'python manage.py syncb' before !"
	exit()


if len(Humor.objects.all()) == 0 :
	# Creating humors
	Humor(name="AFFECTION",  color="rgb(5,176,197)").save()
	Humor(name="ANXIETE",    color="rgb(203,211,0)").save()
	Humor(name="BONHEUR",    color="rgb(229,39,120)").save()
	Humor(name="COLERE",     color="rgb(229,53,45)").save()
	Humor(name="DEPRESSION", color="rgb(200,174,151)").save()
	Humor(name="DOUCEUR",    color="rgb(219,226,235)").save()
	Humor(name="EXCITATION", color="rgb(255,219,13)").save()
	Humor(name="FOLIE",      color="rgb(12,49,131)").save()
	Humor(name="IRRITATION", color="rgb(148,176,128)").save()
	Humor(name="NERVOSITE",  color="rgb(225,142,16)").save()
	Humor(name="PEUR",       color="rgb(112,113,115)").save()
	Humor(name="RAGE",       color="rgb(149,57,125)").save()
	Humor(name="TRISTESSE",  color="rgb(148,203,173)").save()
	print "Humors created"
else : 
	print "Please remove db.sqlite3 and execute 'python manage.py syncb' before !"
	exit()


if len(Note.objects.all()) == 0 :
	# Creating notes
	Note(name="ANIMALE",  color="rgb(200,174,151)").save()
	Note(name="CHIMIQUE", color="rgb(219,226,235)").save()
	Note(name="EPICEE",   color="rgb(216,147,71)").save()
	Note(name="FRUITEE",  color="rgb(203,201,0)").save()
	Note(name="GRASSE",   color="rgb(245,187,211)").save()
	Note(name="VEGETALE", color="rgb(148,203,173)").save()
	print "Notes created"
else : 
	print "Please remove db.sqlite3 and execute 'python manage.py syncb' before !"
	exit()


if len(Image.objects.all()) == 0 :
	# Creating common names
	Image(name="POISSON",             pathImage="images/Image/poisson.png").save()
	Image(name="CHIEN MOUILLE",       pathImage="images/Image/chienMouille.png").save()
	Image(name="BOUC / CHEVRE",       pathImage="images/Image/boucChevre.png").save()
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
	
	
	
	
	
# Save old data in DB (need a parsing function !):

for i in range(21) : Smeller().save()

#Model: Guess(smeller_id='', sample_id='', intensity='', humor_id='', note_id='', image_id='', feeling='', name='').save

Guess(smeller_id=1, sample_id=2, intensity=40, humor_id=5, note_id=5, image_id=2, feeling=20).save()
Guess(smeller_id=2, sample_id=8, intensity=60, humor_id=8, note_id=6, feeling=80).save()
Guess(smeller_id=3, sample_id=8, intensity=20, humor_id=1, note_id=2, image_id=4, feeling=20).save()
Guess(smeller_id=4, sample_id=10, intensity=80, humor_id=10, note_id=2, image_id=16, feeling=60).save()
Guess(smeller_id=5, sample_id=10, intensity=80, humor_id=7, note_id=4, image_id=9, feeling=80).save()
Guess(smeller_id=6, sample_id=13, intensity=80, humor_id=1, note_id=6, feeling=100).save()
Guess(smeller_id=7, sample_id=13, intensity=80, humor_id=9, note_id=3, image_id=16, feeling=60).save()

Guess(smeller_id=8, sample_id=17, intensity=40, humor_id=6, note_id=3, image_id=19, feeling=40).save()
Guess(smeller_id=9, sample_id=20, intensity=80, humor_id=13, note_id=6, image_id=17, feeling=80).save()
Guess(smeller_id=10, sample_id=20, intensity=60, humor_id=6, note_id=4, image_id=8, feeling=60).save()
Guess(smeller_id=11, sample_id=20, intensity=80, humor_id=6, note_id=4, feeling=100).save()
Guess(smeller_id=12, sample_id=20, intensity=80, humor_id=6,  feeling=60, name='rose').save()
Guess(smeller_id=13, sample_id=21, intensity=40, humor_id=6, note_id=4,feeling=60).save()
Guess(smeller_id=14, sample_id=30, intensity=80, humor_id=9, feeling=20).save()

Guess(smeller_id=15, sample_id=31, intensity=40, humor_id=2, note_id=6, image_id=17, feeling=40).save()
Guess(smeller_id=16, sample_id=32, intensity=0, note_id=6, feeling=20).save()
Guess(smeller_id=17, sample_id=41, intensity=60, humor_id=6, note_id=2, image_id=18, feeling=80).save()
Guess(smeller_id=18, sample_id=44, intensity=60, humor_id=6, note_id=4, feeling=80).save()
Guess(smeller_id=19, sample_id=44, intensity=80, humor_id=9, note_id=4, feeling=100).save()
Guess(smeller_id=20, sample_id=45, intensity=60, humor_id=6, note_id=4, feeling=100).save()
Guess(smeller_id=21, sample_id=97, intensity=20, humor_id=6, note_id=3, image_id=16, feeling=60).save()	
