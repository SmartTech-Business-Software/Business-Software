from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("pk", "product_name", "price", "total_number_of_product", "category_name")
