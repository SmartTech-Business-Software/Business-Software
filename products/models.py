from django.db import models
from django.contrib.auth.models import User
from business_area.models import *
# Create your models here.

class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product")
    business = models.ForeignKey(BusinessModel, on_delete=models.CASCADE, related_name="business_product")
    category = models.CharField(max_length=256, null=False, default="Clothing")
    product_name = models.CharField(max_length=256, null=False)
    price = models.DecimalField(max_digits=256, decimal_places=2, null=False)
    quantity = models.IntegerField(null=False)

