from django.urls import path
from shop.api.views import CategoryAPI, BrandAPI, DiscountAPI, ProductAPI

urlpatterns = [
    path('category/', CategoryAPI.as_view(),),
    path('brand/', BrandAPI.as_view(),),
    path('discount/', DiscountAPI.as_view(),),
    path('product/', ProductAPI.as_view(),),
]