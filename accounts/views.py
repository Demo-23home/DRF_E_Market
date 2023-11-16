#Django Imports
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
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
        return Response(serailizer.erorrs)
        


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


