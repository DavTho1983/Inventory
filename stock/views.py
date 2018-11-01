from django.shortcuts import render
import requests
import json
from django.conf import settings
import graphene

# Create your views here.

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return 'Hello ' + name

def orders(request):
    url = 'https://c09bbde4e788c5ada51256bd3ca8e324:856441e5e1bf4fff0f93a8182aa416d0@catsinuniform.myshopify.com/admin/orders.json'
    orders = ((requests.get(url)).json())
    return render(request, 'Stock/home.html', { 'orders': orders })

def inventory(request):
    url = 'https://c09bbde4e788c5ada51256bd3ca8e324:856441e5e1bf4fff0f93a8182aa416d0@catsinuniform.myshopify.com/admin/inventory_items.json?ids=1811692126321'
    inventory = ((requests.get(url)).json())
    print(inventory.keys())
    return render(request, 'Stock/inventory.html', { 'inventory': inventory })

def create(request):
    access_token = '9fd4955c70be6261bf537f9f7ded2687'
    headers = {
        "X-Shopify-Storefront-Access-Token": access_token
    }

    query = """
    {
      shop {
        collections(first: 5) {
          edges {
            node {
              id
              handle
            }
          }
          pageInfo {
            hasNextPage
          }
        }
      }
    }
    """

    data = (requests.post('https://catsinuniform.myshopify.com/api/graphql', json={'query': query}, headers=headers).json())['data']['shop']['collections']['edges']


    print(data)
    return render(request, 'Stock/create.html', { 'create': data })
