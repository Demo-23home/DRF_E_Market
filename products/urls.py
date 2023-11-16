from django.urls import path
from .views import *


urlpatterns = [
    path('products',list_products),
    path('new_product',new_product),    
    path('products/<int:pk>/',get_product),
    path('update_product/<int:pk>/',update_product),
    path('delete_product/<int:pk>/',delete_product),
]
