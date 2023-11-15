from django.urls import path
from .views import *



urlpatterns = [
    path('register/',sign_up),
    path('user_info/',user_info),
]
