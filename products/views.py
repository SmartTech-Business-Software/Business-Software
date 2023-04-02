from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import *
from django.contrib.auth.models import User
from . models import *
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

class CreateProduct(APIView):
    """ View to add a new Product Category """
    def post(self, request):
        data = request.data
        user = request.user
        business = data["business_name"]
        category = data["category"]
        product_name = data["product_name"]
        price = data["price"]
        total_number_of_product = data["quantity"]
        user_data = User.objects.filter(username = user.username).values()
        business_data = BusinessModel.objects.filter(business_name=business).values()
        userId = user_data[0]["id"]
        businessId = business_data[0]["id"]
        if userId and businessId:
            product = Products(user_id = userId, business_id = businessId, product_name = product_name, price = price, quantity=total_number_of_product, category = category)
            product.save()
            return Response(data={
                "status": status.HTTP_201_CREATED,
                "msg": "product successfully created"
            })
        return Response(data={
            "status": status.HTTP_400_BAD_REQUEST
        })

class RetrieveListProducts(generics.ListAPIView):
    """ View to list all Categories"""
    def get(self, request):
        user = request.user
        user_data = User.objects.filter(username = user).values()
        userID = user_data[0]['id']
        products = Products.objects.filter(user_id = userID)
        serializer = ProductSerializer(products, context={"request": request}, many=True)
        if serializer:
            return Response(data={
                "status": status.HTTP_200_OK,
                "products": serializer.data
            })
        return Response(data={
            "status": status.HTTP_400_BAD_REQUEST,
            "error": serializer.error
        })

class RetriveProduct(generics.RetrieveAPIView):
    """ View to retrieve products"""
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


class RetrieveProductByCategory(APIView):
    def post(self, request):
        data = request.data
        user = request.user
        user_data = User.objects.filter(username = user).values()
        userID = user_data[0]["id"]
        category = data["category"]

        products = Products.objects.filter(user_id = userID).filter(category_name = category)
        serializer = ProductSerializer(products, context={"request": request}, many=True)
        if products:
            return Response(data={
                "status": status.HTTP_200_OK,
                "products": serializer.data
            })
        return Response(data={
            "status": status.HTTP_400_BAD_REQUEST,
            "msg": "category dosent exist"
        })

class UpdateProduct(generics.UpdateAPIView):
    """ View to update Products"""
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class DeleteProduct(generics.DestroyAPIView):
    """ View to delete product """
    def delete(self, request, pk):
        product = Products.objects.filter(pk = pk)
        if product:
            product.delete()
            return Response(data={
                "status":status.HTTP_200_OK,
                "msg": "Product successfully deleted"
            })
        return Response(data={
            "status": status.HTTP_400_BAD_REQUEST,
            "msg": 'product not found'
        })
        

class TotalProducts(APIView):
    """ View to get the toal number of products """
    def post(self, request):
        data = request.data
        user = request.user
        user_data = User.objects.filter(username=user).values()
        userId = user_data[0]["id"]
        products = Products.objects.filter(user_id = userId).values()
        if products:
            list_number_of_product = []
            for x in products:
                number_of_product = x["total_number_of_product"]
                list_number_of_product.append(number_of_product)
            total = sum(list_number_of_product)
            return Response(data={
                "total": total,
                "status": status.HTTP_200_OK,
                "msg": "success"
            })
        return Response(data={
            "total": 0,
            "status":status.HTTP_200_OK,
            "msg": "No products available"
        })
        



