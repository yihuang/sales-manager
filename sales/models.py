# coding: utf-8
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Region(models.Model):
    name = models.CharField(u'区域名', max_length=128)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = u'区域'


class City(models.Model):
    region = models.ForeignKey(Region, verbose_name=u'区域')
    name = models.CharField(u'城市名', max_length=128)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = u'城市'


class Shop(models.Model):
    city = models.ForeignKey(City, verbose_name=u'城市')
    name = models.CharField(u'店名', max_length=128)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = u'店铺'


class Employee(models.Model):
    user = models.OneToOneField(User)
    shop = models.ForeignKey(Shop, verbose_name=u'店铺')

    class Meta:
        verbose_name = verbose_name_plural = u'员工'


class Brand(models.Model):
    name = models.CharField(u'品牌', primary_key=True, max_length=128)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = u'品牌'


class Product(models.Model):
    no = models.CharField(u'编号', max_length=32, primary_key=True)
    name = models.CharField(u'产品名', max_length=128)
    date = models.DateField(u'上市日期')
    price = models.DecimalField(u'零售价格', decimal_places=2, max_digits=9)
    brand = models.ForeignKey(Brand)

    def __unicode__(self):
        return self.name

    def isnew(self):
        return (datetime.now() - self.date).days

    class Meta:
        verbose_name = verbose_name_plural = u'产品'


class SaleData(models.Model):
    product = models.ForeignKey(Product, verbose_name=u'产品')
    price = models.DecimalField(u'销售价格', decimal_places=2, max_digits=9)
    shop = models.ForeignKey(Shop, verbose_name=u'店铺')
    created_by = models.ForeignKey(User, verbose_name=u'员工')
    sale_at = models.DateTimeField(u'销售时间')

    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)

    class Meta:
        verbose_name = verbose_name_plural = u'销售流水'
