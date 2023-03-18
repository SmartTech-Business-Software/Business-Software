from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("create_product/", CreateProduct.as_view(), name="create_product"),
    path("retrieve_product/<int:pk>", RetriveProduct.as_view(), name="retrieve_product"),
    path("retrieve_product/", RetrieveListProducts.as_view(), name="retrieve_products"),
    path("total_product/", TotalProducts.as_view
    (), name="total_products"),
    path("retrieve_by_category/", RetrieveProductByCategory.as_view(), name="retrieve_by_category")
]