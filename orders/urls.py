from django.urls import path
from .views import *



urlpatterns = [
    path('new_order/', new_order),
    path('list_orders/', list_orders),
    path('get_order/<int:pk>/', get_order),
    path('update_order/<int:pk>/', update_order),
    path('delete_order/<int:pk>/', delete_order),
]
