#Rest imports
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
#django imports
from django.shortcuts import get_object_or_404
from django.db.models import Avg
#internal imports
from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer
from .filters import ProductsFilter
# Create your views here.


@api_view(['GET'])
def list_products(request):
    filter_set = ProductsFilter(request.GET, queryset=Product.objects.all().order_by('id'))
    res_page = 12
    count = filter_set.qs.count()
    paginator = PageNumberPagination()
    paginator.page_size = res_page
    queryset = paginator.paginate_queryset(filter_set.qs, request)
    serializer = ProductSerializer(queryset, many=True)

    json = {
        "Prodcuts":serializer.data
        }
    return Response(json, status=status.HTTP_200_OK)



@api_view(['GET'])
def get_product(request, pk):
    product = get_object_or_404(Product,id=pk)
    serializer = ProductSerializer(product)
    # print(products)
    json = {
        "Prodcut":serializer.data
        }
    return Response(json, status=status.HTTP_200_OK)

    

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def new_product(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        product = serializer.save(user=request.user)
        res_serializer = ProductSerializer(product, many=False)
        return Response({"Product": res_serializer.data})
    
    return Response(serializer.errors)

    


@api_view(["PUT"])
@permission_classes([IsAuthenticated,IsAdminUser])
def update_product(request, pk):
    product = get_object_or_404(Product,id=pk)

    if product.user != request.user:
        return Response({"Error":"you can't update this product"},status=status.HTTP_401_UNAUTHORIZED)
    
    product_serializer = ProductSerializer(instance=product, data=request.data, partial=True)

    if not product_serializer.is_valid():
        return Response({"Error":"not valid data"},status=status.HTTP_400_BAD_REQUEST)
    
    product_serializer.save()
    return Response({"Product":product_serializer.data},status=status.HTTP_200_OK)




@api_view(['DELETE'])
@permission_classes([IsAuthenticated,IsAdminUser])
def delete_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    product.delete()
    if request.user == product.user:
        product.delete
        return Response({"Deleted":"your Product has been deleted"}, status=status.HTTP_200_OK)
    return Response({"Error":"sorry you can't delete this product"}, status=status.HTTP_401_UNAUTHORIZED)




@api_view(["POST","GET"])
@permission_classes([IsAuthenticated])
def new_review(request, pk):
    data = request.data
    user = request.user
    product = get_object_or_404(Product, id=pk)
    print(product)
    # return Response({'product'})
    review = product.reviews.filter(user=user).first()
    print(review)
    if review:
        review_serializer = ReviewSerializer(instance=review, data=data, partial=True)
        if review_serializer.is_valid():
            rate = product.reviews.aggregate(avg_ratings=Avg('rate'))
            product.rate = rate['avg_ratings']
            product.save()
            review_serializer.save(user=user, product=product)
            return Response({"details":"product review updated","data":review_serializer.data})
    
        return Response({"Errors":review_serializer.errors})
    
    review_serializer = ReviewSerializer(data=data)
    if review_serializer.is_valid():
        review_serializer.save(user=user,product=product)
        return Response({"details":"product review created"},status=status.HTTP_200_OK)
    return Response({"Errors":review_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)






@api_view(['DELETE'])
@permission_classes([IsAuthenticated,IsAdminUser])
def delete_review(request, pk):
    user = request.user
    product = get_object_or_404(Product, id=pk)
    review = product.reviews.filter(user=user)

    if review:
        review.delete()
        rate = product.reviews.aggregate(avg_ratings=Avg('rate'))
        if rate['avg_ratings'] is None:
            rate['avg_ratings'] = 0
            product.rate = rate['avg_ratings']
            product.save()
            return Response({"details":"product review  has been deleted"})
        return Response({"Error":"review is not found"}, status=status.HTTP_404_NOT_FOUND)








    