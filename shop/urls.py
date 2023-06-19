from django.urls import path
from shop.views import Shop_list_view, Order_view

urlpatterns=[
    path('', Shop_list_view, name='shop'),
    path('order/', Order_view, name='order'),
]