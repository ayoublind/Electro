
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # ex: /product/5/
    path('<int:product_id>/', views.product),
    #path('contact/', views.contact, name='contact'),
]
