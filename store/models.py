from django.db import models

import datetime
from django.utils import timezone
# Create your models here.

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

#
class Product(models.Model):

    name = models.CharField(max_length=50, default='')
    date = models.DateField('date published', default='none')
    offer = models.BooleanField(default=False)
    pourcentage = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    description = models.TextField(default='')
    prix = models.FloatField(default=0.0)
    prix_old = models.FloatField(default=0.0)
    # SET_DEFAULT si une categorie a été suprimée dans la table 'Categorie', les produits de cette catégorie 
    # ne seront pas suprimé et la valeur du leurs champ categorie sera 'none'
    categorie =  models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return "produit"

class Image(models.Model):
    url = models.CharField(max_length=50, default='')
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.url


class User(models.Model):
    username = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')
    firstname = models.CharField(max_length=50, default='')
    lastname = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    tel = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.username

class Panier(models.Model):

    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    qte = models.IntegerField()

    def __str__(self):
        return self.qte

class Facture(models.Model):

    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total = models.FloatField()
    checked = models.BooleanField(default=False)

    def __str__(self):
         return self.total

class Commande(models.Model):
    nb_prod = models.IntegerField(default=0)
    total = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.total


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
