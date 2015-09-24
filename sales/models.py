from django.db import models
from django.contrib.auth.models import User


class Region(models.Model):
    name = models.CharField(max_length=128)


class City(models.Model):
    region = models.ForeignKey(Region)
    name = models.CharField(max_length=128)


class Shop(models.Model):
    city = models.ForeignKey(City)
    name = models.CharField(max_length=128)


class Employee(models.Model):
    user = models.OneToOneField(User)
    shop = models.ForeignKey(Shop)


class Product(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=128)


class SaleData(models.Model):
    product = models.ForeignKey(Product)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    shop = models.ForeignKey(Shop)
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
