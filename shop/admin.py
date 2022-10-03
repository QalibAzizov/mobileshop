from django.contrib import admin
from shop.models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
     list_display = ('first_name','last_name','email','phone')
     list_filter = ['created_at']
     search_fields =('first_name','last_name',)


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
     list_display = ('title','code','price',)
     list_filter = ['created_at']
     search_fields =('title','code','price',)


@admin.register(Discount)
class DiscountAdmin(TranslationAdmin):
     list_display = ('title','percentage',)
     list_filter = ['created_at']
     search_fields =('title','percentage',)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('title',)
    list_filter = ['created_at']
    search_fields =('title','created_at',)

@admin.register(Brand)
class BrandAdmin(TranslationAdmin):
    list_display = ('title',)
    list_filter = ['created_at']
    search_fields =('title','created_at',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    
     list_filter = ['created_at']


