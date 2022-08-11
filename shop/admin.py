from django.contrib import admin
from shop.models import *
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
     list_display = ('title','code','price',)
     list_filter = ['created_at']
     search_fields =('title','code','price',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
     list_display = ('title','percentage',)
     list_filter = ['created_at']
     search_fields =('title','percentage',)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ['created_at']
    search_fields =('title','created_at',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ['created_at']
    search_fields =('title','created_at',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    
     list_filter = ['created_at']