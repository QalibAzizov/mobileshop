from django.urls import path
from shop.views import home,product,checkout,store,blank

 


urlpatterns = [
    path('', home, name='home'),
    path('product/<slug:slug>', product, name='product'),
    path('checkout', checkout, name='checkout'),
    path('store', store, name='store'),
    path('blank', blank, name='blank'),
   
    
]