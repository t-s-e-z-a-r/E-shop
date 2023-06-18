from django.urls import path
from users.views import HomeView, SignUpView

from shop.views import Shop_list_view, Order_view
from . import views

urlpatterns=[
    path('', Shop_list_view, name='shop'),
    path('order/', Order_view, name='order'),
]