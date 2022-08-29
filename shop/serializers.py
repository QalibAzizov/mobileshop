from rest_framework import serializers
from shop.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'slug'
        )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'title',
            'slug'
        )    


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = (
            'id',
            'title',
            'slug'
        )  


class ProductSerializer(serializers.ModelSerializer):
    # brand = BrandSerializer()
    # category = CategorySerializer()

    brand = serializers.CharField(source = 'brand.title')
    category = serializers.CharField(source = 'category.title')
   
    class Meta:
        model = Product
        fields = (
            'id',
            'brand',
            'image',
            'category',
            'title',
            'slug',
            'price',
            'sellprice',
            'description',
            'discount',
            'created_at',
            'updated_at'
        )  