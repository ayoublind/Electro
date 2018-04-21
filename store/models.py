from django.db import models

import datetime
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    def __str__(self):
        return "produit"

class Image(models.Model):
    def __str__(self):
        return "Image"

class User(models.Model):
    def __str__(self):
        return "User"

class Panier(models.Model):
    def __str__(self):
        return "Panier"

class Facture(models.Model):
    def __str__(self):
        return "Facture"

class Commande(models.Model):
    def __str__(self):
        return "commande"

# la classe categorie 
class Categorie(models.Model):
    designation = models.CharField(max_length=200)
    
    def __str__(self):
        return self.designation
        
#
class SousCategorie(models.Model):
    cat = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    designation = models.CharField(max_length=200)

    def __str__(self):
        return self.designation

#la classe review pour presenter les observations des utilisateurs sur chaque produit
class Review(models.Model):
    note = models.IntegerField(default=0)
    date = models.DateField('date review')
    comment = models.CharField(max_length=800)
    #cles etrangers vers les tables : produit et user
    # cascade pour indiquer que si on supprime un produit par exp, le review doit etre supprimer automatiquement
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #on veut afficher que la note lors de l'appele de la methode tostring(affichage)
    def __str__(self):
        return self.note
