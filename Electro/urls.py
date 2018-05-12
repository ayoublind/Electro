

"""Electro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import login

from store import views


#import
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #page principale de l'application
    path('',views.index),
    #les produits
    path('products/',include('store.urls')),
    #shop
    path('shop/',views.shop),
    #blog
    path('blog/',views.blog),
    #cart
    path('cart/',views.cart),
    #contact
    path('contact/',views.contact),
    #regular
    path('regular/', views.regular),
    #login/logout
    path('logout/', views.logoutPage),
    path('login/', login , {'template_name': 'login.html'}),
    #register
    path('register/', views.register),
    #wishlist
    path('wishlist/', views.wishlist),
    #about us
    path('about/', views.about),

     # ex: /categorie/1/
    path('categorie/<int:categorie_id>/', views.categorie),
    #administrator page
    path('admin/', admin.site.urls),
]


#make it on debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)