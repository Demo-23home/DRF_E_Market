from django.urls import path
from .views import *


urlpatterns = [
    path('products',list_products),
    path('products/<int:pk>/',list_product),
]
