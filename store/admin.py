from django.contrib import admin
from .models import Categorie, SousCategorie, Review,Product, User, Image, Panier, Facture, Commande

# Register your models here.
admin.site.register(Categorie)
admin.site.register(SousCategorie)
admin.site.register(Review)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Image)
admin.site.register(Panier)
admin.site.register(Facture)
admin.site.register(Commande)