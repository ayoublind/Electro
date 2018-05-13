from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect

from .models import Product, Categorie, Image, Marque

from django.db.models import Count
from django.db.models import Q
from django.contrib.auth import logout

# Create your views here.

def index(request):
    featured_product_list = Product.objects.order_by('-pourcentage')[:5]
    latest_product_list = Product.objects.order_by('-date')[:10]
    orders_product_list = Product.objects.order_by('-orders')[:10]
    products = Product.objects.all()

    all_product = Product.objects.all()

    query = request.GET.get("query")
    if query:
        all_product = all_product.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(prix__icontains=query)
            ).distinct()

    context = {'featured_product_list' : featured_product_list
                , 'latest_product_list' : latest_product_list
                ,'orders_product_list' : orders_product_list
                ,'products':products}
    return render(request, 'index.html',context)

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product.html', {'product':product})

#page charger for categorie
def categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, pk=categorie_id)
    return render(request, 'categorie.html', {'categorie':categorie})

# view pour charger la liste des produit par marque
def marques(request, marque_id):
    marque = get_object_or_404(Marque, pk=marque_id)
    return render(request, 'marque.html', {'marque':marque})

def shop(request):
    return render(request, 'shop.html')

def blog(request):
    return render(request, 'blog.html')

def cart(request):
    return render(request, 'cart.html')
	
def contact(request):
	return render(request, 'contact.html')

def regular(request):
	return render(request, 'regular.html')

def register(request):
	return render(request,'register.html')


def logoutPage(request):
    logout(request)
    return HttpResponseRedirect('/')


#wishlist fonction
def wishlist(request):
    return render(request, 'wishlist.html')

#about us
def about(request):
    return render(request, 'about.html')

