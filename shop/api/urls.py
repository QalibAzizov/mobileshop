from django.urls import path
from shop.api.views import CategoryAPI, BrandAPI, DiscountAPI, ProductAPI,ProductDetailAPI

urlpatterns = [
    path('category/', CategoryAPI.as_view(),),
    path('brand/', BrandAPI.as_view(),),
    path('discount/', DiscountAPI.as_view(),),
    path('products/', ProductAPI.as_view(),),
    path('product/<int:pk>', ProductDetailAPI.as_view(),),
]