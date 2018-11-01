from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    sku = models.CharField(max_length=3, blank=True, null=True)
    requires_shipping = models.BooleanField(default=False)
    weight_in_grams = models.IntegerField(blank=True, null=True)
    no_in_stock = models.IntegerField(default=0)
