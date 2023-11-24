from django.urls import path
from .views import *



urlpatterns = [
    path('register/',sign_up),
    path('user_info/',user_info),
    path('update_user/',update_user),
    path('forgot_password/', forget_password,name='forgot_password'), 
    path('reset_password/<str:token>', reset_password,name='reset_password'), 
]
