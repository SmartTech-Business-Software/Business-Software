from rest_framework import serializers
from django.contrib.auth.models import User

class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("pk", "username", "password", "email", "first_name", "last_name")