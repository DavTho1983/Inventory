from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('products', views.products, name='products'),
]
