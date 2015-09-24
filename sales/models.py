from django.db import models

class Product(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=128)

class SaleData(models.Model):
    product = models.ForeignKey(Product)

