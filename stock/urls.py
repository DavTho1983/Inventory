from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('inventory', views.inventory, name='inventory'),
    path('create', views.create, name='create'),
]
