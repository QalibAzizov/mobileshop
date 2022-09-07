from django.urls import path
from shop.api.views import(
    CategoryAPI,
    BrandAPI, 
    DiscountAPI, 
    ProductAPI,
    ProductDetailAPI 
    
) 

urlpatterns = [
    path('categories/', CategoryAPI.as_view(),),
    path('brands/', BrandAPI.as_view(),),
    path('discounts/', DiscountAPI.as_view(),),
    path('products/', ProductAPI.as_view(),),
    path('products/<int:pk>', ProductDetailAPI.as_view(),),
]