from django.contrib import admin
from . models import *

# Register your models here.

@admin.register(BusinessModel)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ("user", "business_name", "business_type",)


