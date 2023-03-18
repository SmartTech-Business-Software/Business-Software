from django.db import models
from django.contrib.auth.models import User
from business_area.models import *

# Create your models here.

class Expenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_expense")
    business = models.ForeignKey(BusinessModel, on_delete=models.CASCADE, related_name="business_expense")
    expense = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    amount = models.CharField(max_length=255, null=False)
    date = models.DateField(auto_now_add=True, null=False)
    

