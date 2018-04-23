from django.db import models

import datetime
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField('added date')
    offer = models.BooleanField()
    pourcentage = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    prix = models.FloatField()
    prix_old = models.FloatField()
    # SET_DEFAULT si une categorie a été suprimée dans la table 'Categorie', les produits de cette catégorie 
    # ne seront pas suprimé et la valeur du leurs champ categorie sera 'none'
    categorie =  models.ForeignKey('Categorie', on_delete=models.SET_DEFAULT, default='none')
 
    def __str__(self):
        return "produit"

class Image(models.Model):
    url = models.CharField(max_length=50)
    prod =  models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.url


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)

    def __str__(self):
        return self.username

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
