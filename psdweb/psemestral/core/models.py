from django.db import models


# Create your models here.

class user(models.Model):
    
    nom = models.CharField( max_length=50)
    snom = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    password = models.CharField( max_length=50)

    def __str__(self):
        return self.email

class contacto(models.Model):

    name = models.CharField( max_length=50)
    email = models.CharField( max_length=200)
    msn = models.CharField( max_length=300)

    def __str__(self):
        return self.name
        