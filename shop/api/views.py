from multiprocessing import context
from rest_framework.views import APIView
from rest_framework.response import Response
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
        discounts= Product.objects.all()
        serializer = ProductSerializer(discounts, many=True , context ={'request': self.request})
        
        return Response(data = serializer.data)