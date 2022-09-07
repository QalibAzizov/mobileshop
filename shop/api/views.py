from multiprocessing import context
from unicodedata import category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK)
from django.http import Http404
from shop.serializers import CategorySerializer, BrandSerializer,DiscountSerializer, ProductSerializer
from shop.models import *



class CategoryAPI(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories,many=True)
        
        return Response(data = serializer.data)


class BrandAPI(APIView):
    def get(self, request, *args, **kwargs):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        
        return Response(data = serializer.data)


class DiscountAPI(APIView):
    def get(self, request, *args, **kwargs):
        discounts= Discount.objects.all()
        serializer = DiscountSerializer(discounts, many=True)
        
        return Response(data = serializer.data)


class ProductAPI(APIView):
    def get(self, request, *args, **kwargs):
        products= Product.objects.all()
        category = request.GET.get('category')
        brand = request.GET.get('brand')
        if category:
            products= Product.objects.filter(category__id=category)
            if not products:
                raise Http404

        if brand:
            products= Product.objects.filter(brand__id=brand)
            if not products:
                raise Http404
            
        serializer = ProductSerializer(products, many=True , context ={'request': self.request})
        
        return Response(data = serializer.data)


class ProductDetailAPI(APIView):
    def get(self, request, *args, **kwargs):
            product= Product.objects.filter(id=kwargs['pk']).first()
            if not product:
                raise Http404
            serializer = ProductSerializer(product,  context ={'request': self.request})
            return Response(data = serializer.data, status=HTTP_200_OK)    
            




