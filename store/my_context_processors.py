
from .models import Categorie, Product, Marque, Panier


def include_categories(request):
    #perform your logic to create your list of groups
    categories = Categorie.objects.order_by('-designation')
    return {'categories':categories}

#all products
def include_products(request):
    products = Product.objects.order_by('-designation')
    return {'products':products}

#all marques
def include_marques(request):
    marques = Marque.objects.order_by('-name')
    return {'marques':marques}

#all panier
def include_panier(request):
    panier = Panier.objects.order_by('-id_product')
    return {'panier':panier}