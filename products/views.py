#Rest imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
#django imports
from django.shortcuts import render
from django.shortcuts import get_object_or_404
#internal imports
from .models import Product
from .serializers import ProductSerailzer
from .filters import ProductsFilter
# Create your views here.


@api_view(['GET'])
def list_products(request):
    filter_set = ProductsFilter(request.GET, queryset=Product.objects.all().order_by('id'))
    res_page = 2
    paginator = PageNumberPagination()
    paginator.page_size = res_page
    queryset = paginator.paginate_queryset(filter_set.qs, request)
    serializer = ProductSerailzer(queryset, many=True)

    json = {
        "Prodcuts":serializer.data
        }
    return Response(json, status=status.HTTP_200_OK)

@api_view(['GET'])
def list_product(request, pk):
    product = get_object_or_404(Product,id=pk)
    serializer = ProductSerailzer(product)
    # print(products)
    json = {
        "Prodcut":serializer.data
        }
    return Response(json, status=status.HTTP_200_OK)
