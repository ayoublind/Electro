from django.contrib import admin
from .models import Categorie, SousCategorie, Review

# Register your models here.
admin.site.register(Categorie)
admin.site.register(SousCategorie)
admin.site.register(Review)