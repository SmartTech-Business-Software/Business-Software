from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("create_business/", CreateBusiness.as_view(), name="business_area"),
    path("retrieve_business_info/<int:pk>", RetrieveBusiness.as_view(), name="retrieve_buisness"),
    path("update_business/<int:pk>", UpdateBusiness.as_view(), name="update_business"),
    path("retrieve_list_business/", RetrieveListBusiness.as_view(), name="retrieve_list_business"),
    path("delete_business/<int:pk>", DeleteBusiness.as_view(), name="delete_business")
]