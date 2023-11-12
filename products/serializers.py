from rest_framework import serializers

from .models import Product



class ProductSerailzer(serializers.ModelSerializer):
   
    class Meta:
        model = Product
        fields = ('name', 'price', 'brand')