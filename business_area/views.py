from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import *
from django.contrib.auth.models import User
from . models import *

# Create your views here.

class CreateBusiness(generics.CreateAPIView):
    """ View to create business information """
    def post(self, request):
        data = request.data
        user = request.user
        # print(f"---> {user}")
        business_name = data["business_name"]
        business_type = data["business_type"]
        user_data = User.objects.filter(username = user.username).values()
        # print(f"data----> {user_data}")
        userId = user_data[0]["id"]
        if userId:
            business = BusinessModel.objects.create(user_id = userId,  business_name=business_name, business_type = business_type)
            business.save()
            serializer = BusinessSerializer(business, context={"request": request})
            return Response(data={
                "status": status.HTTP_201_CREATED,
                "business": serializer.data
            })
        return Response(data={
            "status": status.HTTP_400_BAD_REQUEST
        })


class RetrieveBusiness(generics.RetrieveAPIView):
    """ View to retrieve business information """
    queryset = BusinessModel.objects.all()
    serializer_class = BusinessSerializer
    lookup_field = "pk"

class UpdateBusiness(generics.UpdateAPIView):
    """ View to update business information """
    queryset = BusinessModel.objects.all()
    serializer_class = BusinessSerializer

class DeleteBusiness(generics.DestroyAPIView):
    """ View to delete business """
    queryset = BusinessModel.objects.all()
    serializer_class = BusinessSerializer

class RetrieveListBusiness(APIView):
    """ View to Retrive List of Registered Business """
    def get(self, request):
        user = request.user
        user_data = User.objects.filter(username = user.username).values()
        userID = user_data[0]["id"]
        businesses = BusinessModel.objects.filter(user_id = userID)
        serializer = BusinessSerializer(businesses, context={"request":request}, many=True)
        if serializer:
            return Response(data={
                "status": status.HTTP_200_OK,
                "businesses": serializer.data
            })
        return Response(data={
            "status": status.HTTP_400_BAD_REQUEST,
            "msg": "No business found"
        })