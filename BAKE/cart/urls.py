from django.urls import path
from .views import *
urlpatterns = [
    path('order', order, name='order'),
    path('cart', cart, name='cart'),
]