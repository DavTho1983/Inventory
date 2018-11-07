from django.shortcuts import render
import requests
import json
from django.conf import settings

from .forms import OrderForm

# Create your views here.

def get_orders():
    return (requests.get(settings.ORDERS_URL)).json()

def get_products():
    return requests.get(settings.PRODUCTS_URL).json()['products']

def products(request):
    products = requests.get(settings.PRODUCTS_URL).json()
    return render(request, 'Stock/products.html', products)

def map_product_title_to_var_id(products):
    product_mapping = []
    for product in products:
        product_mapping.append((product['variants'][0]['id'], product['variants'][0]['inventory_item_id']))
    return product_mapping

def get_product_titles(products):
    product_titles = []
    for product in products:
        product_titles.append(product['title'])
    return product_titles

def orders(request):
    orders = get_orders()
    products = get_products()
    mapping = map_product_title_to_var_id(products)
    product_titles = get_product_titles(products)
    if request.method == 'POST':
        form = OrderForm(data=request.POST, products=product_titles)
        if form.is_valid():
            var_id = mapping[int(form.cleaned_data['product_name'])][0]
            quantity = form.cleaned_data['quantity']
            order = {
              "order": {
                "line_items": [
                  {
                    "variant_id": var_id,
                    "quantity": quantity
                  }
                ]
              }
            }
            # locations = requests.get('https://758717f3860d439f8355c22e91271bd8:859fb17c0f4953fcc606303d0bef4191@catsinuniform.myshopify.com/admin/locations.json')
            # print(list(locations))
            if quantity > 0:
                requests.post(settings.ORDERS_URL, json=order)
                item_id = mapping[int(form.cleaned_data['product_name'])][1]
                inventory_levels = {
                    "location_id": 19639369841,
                    "inventory_item_id": item_id,
                    "available_adjustment": -quantity
                }
                requests.post(settings.INVENTORY_URL, json=inventory_levels)
    else:
        form = OrderForm(quantity=0)
    return render(request, 'Stock/home.html', {'orders': orders, 'form': form})
