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

admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)

admin.site.register((Product, SaleData, Region, City, Shop))
