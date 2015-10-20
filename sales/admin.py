from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'


class NewUserAdmin(UserAdmin):
    inlines = (EmployeeInline, )


@admin.register(SaleData)
class SaleDataAdmin(admin.ModelAdmin):
    list_filter = ('created_at', 'shop__name', 'shop__city__name', 'shop__city__region__name', 'product__brand__name', 'product__name')
    list_display = ('product', 'shop', 'price', 'created_by', 'sale_at')

admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)

admin.site.register((Brand, Product, Region, City, Shop))
