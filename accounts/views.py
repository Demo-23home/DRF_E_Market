#Django Imports
from datetime import datetime, timedelta
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
#Rest Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
#Internal Imports
from .serializers import UserSerializer, SignUpSerializer

# Create your views here.
@api_view(['POST'])
def sign_up(request):
    data = request.data
    serailizer = SignUpSerializer(data=data)

    if serailizer.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user = User.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                username = data['username'],
                email = data['email'],
                password = make_password(data['password']),
                  )
            return Response ({
               'details': 'Your Account has been created successfully!',}
               ,status=status.HTTP_200_OK
            )
        return Response({'details':'A user with this email already exists'},
                        status=status.HTTP_400_BAD_REQUEST
                        )
    else:
        return Response({"details":"not a valid data"}, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    serailizer = UserSerializer(request.user, many=False)
    return Response(serailizer.data)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user

    if 'password' in request.data:
        password = make_password(request.data.get('password'))
        user.set_password(password)

    serializer = UserSerializer(instance=user, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




def get_current_host(request):
    protocol = request.is_secure() and 'https' or 'http'
    host = request.get_host()

    return f'{protocol}//{host}'



@api_view(['POST'])
def forget_password(request):
    data = request.data
    user = get_object_or_404(User,email=data['email'])
    token = get_random_string(40)
    expire_date = datetime.now() + timedelta(minutes=30)
    user.profile.reset_password_token = token
    user.profile.reset_password_expire = expire_date
    user.profile.save()
    
    host = get_current_host(request)
    link = "http://localhost:8000/accounts/reset_password/{token}".format(token=token)
    body = "Your password reset link is : {link}".format(link=link)
    send_mail(
        "Paswword reset from eMarket",
        body,
        "eMarket@gmail.com",
        [data['email']]
    )
    return Response({'details': 'Password reset sent to {email}'.format(email=data['email'])})






@api_view(['POST'])
def reset_password(request,token):
    data = request.data
    user = get_object_or_404(User,profile__reset_password_token = token)

    if user.profile.reset_password_expire.replace(tzinfo=None) < datetime.now():
        return Response({'error': 'Token is expired'},status=status.HTTP_400_BAD_REQUEST)
    
    if data['password'] != data['confirmPassword']:
        return Response({'error': 'Password are not same'},status=status.HTTP_400_BAD_REQUEST)
    
    user.password = make_password(data['password'])
    user.profile.reset_password_token = ""
    user.profile.reset_password_expire = None 
    user.profile.save() 
    user.save()
    return Response({'details': 'Password reset done '})