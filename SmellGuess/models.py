from django.db import models




# TO DO: Change the fields (Lucas or Flo ?)
class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")



  
# TO DO: Change the fields (Lucas or Flo ?)
class Sample(models.Model):
    name = models.CharField(max_length=42)
    intensity = models.CharField(max_length=42)