from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BusinessModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="business_page")
    business_name = models.CharField(max_length=356, null=False)
    business_type = models.CharField(max_length=256, null=False)





