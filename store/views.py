from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Product

# Create your views here.


def index(request):
    featured_product_list = Product.objects.order_by('-pourcentage')[:5]
    latest_product_list = Product.objects.order_by('-date')[:10]
    orders_product_list = Product.objects.order_by('-orders')[:10]
    context = {'featured_product_list' : featured_product_list
                , 'latest_product_list' : latest_product_list
                ,'orders_product_list' : orders_product_list}
    return render(request, 'index.html',context)

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product.html', {'product': product})

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

def sign_in(request):
	return render(request, 'sign_in.html')

def register(request):
	return render(request,'register.html')