from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
	sex = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=1000)