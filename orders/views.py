from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
#django imports
from django.shortcuts import get_object_or_404 
#internal imports
from .models import *
from .serializers import *
from products.models import Product
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_order(request):
    user = request.user 
    data = request.data
    order_items = data['order_Items']

    if order_items and len(order_items) == 0:
       return Response({'error': 'No order recieved'},status=status.HTTP_400_BAD_REQUEST)
    else:
        total_amount = sum( item['price']* item['quantity'] for item in order_items)
        order = Order.objects.create(
            user = user,
            city = data['city'],
            zip_code = data['zip_code'],
            street = data['street'],
            phone_no = data['phone_no'],
            country = data['country'],
            total_amount = total_amount,
        )
        for i in order_items:
            product = Product.objects.get(id=i['product'])
            item = OrderItem.objects.create(
                product= product,
                order = order,
                name = product.name,
                quantity = i['quantity'],
                price = i['price']
            )
            product.stock -= item.quantity
            product.save()
        serializer = OrderSerializer(order,many=False)
        return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_orders(request):
    orders = Order.objects.all()
    order_serailizer = OrderSerializer(orders, many=True)
    return Response({"Orders: ":order_serailizer.data}, status=status.HTTP_200_OK)


    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order(request, pk):
    order = get_object_or_404(Order, id=pk)
    order_serializer = OrderSerializer(order,many=False)
    return Response(order_serializer.data)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated,IsAdminUser])
def delete_order(request, pk):
    try:
        order = Order.objects.get(id=pk)
    except:
        return Response({"Errors":f"order with id {pk} is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    order.delete()
    return Response({"details":"order has been deleted"},status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsAdminUser])
def update_order(request,pk):
    try:
        order = Order.objects.get(id=pk)
    except:
        return Response({"Errors":f"order with id {pk} is not found"}, status=status.HTTP_404_NOT_FOUND)
    order.status = request.data['status']
    order.save()
    return Response({"details":"order status has been updated"})