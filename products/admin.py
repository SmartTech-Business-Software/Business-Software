from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("user", "business", "pk", "product_name", "price", "quantity",)

