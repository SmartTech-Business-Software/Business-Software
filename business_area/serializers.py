from rest_framework import serializers
from .models import *

class BusinessSerializer(serializers.ModelSerializer):
    """ Serializer to serialize the business information """
    class Meta:
        model = BusinessModel
        fields = ("pk", "business_name", "business_type")