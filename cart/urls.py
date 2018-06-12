from django.conf.urls import url

from .views import (
    add_to_cart,
    delete_from_cart,
    order_details,
)

app_name = 'cart'

urlpatterns = [
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    url(r'^order-summary/$', order_details, name="order_summary"),
]