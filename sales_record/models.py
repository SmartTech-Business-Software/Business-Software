from django.db import models
from django.contrib.auth.models import User
from business_area.models import *

# Create your models here.

class SalesRecords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sales")
    business = models.ForeignKey(BusinessModel, on_delete=models.CASCADE, related_name="business_sales")
    product_sold = models.CharField(max_length=256, null=False)
    product_category = models.CharField(max_length=256, null=False)
    price_of_product = models.DecimalField(max_digits=256, decimal_places=2, null=False)
    price_sold_at = models.DecimalField(max_digits=256, decimal_places=2, null=False)
    quantity_sold = models.IntegerField(null=False)
    total = models.DecimalField(max_digits=255, decimal_places=2, null=False, default=1000.00)
    date_sold = models.DateTimeField(auto_now_add=True)

