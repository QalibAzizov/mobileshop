from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from shop.models import*

# Create your views here.

def home(request):
    # product= Product.objects.all()
    category = Category.objects.all()
    brand = Brand.objects.all()
    category_id = request.GET.get('category') 
    if category_id:
        product = Product.objects.filter(category = category_id)
    else:
        product= Product.objects.all()

       
    context = {
        'product': product,
        'category': category,
        'brand ' : brand ,
    
    }

    return render(request,'index.html', context)


def store(request):
    product= Product.objects.all()
    category = Category.objects.all()
    brand = Brand.objects.all()

    context = {
       
        'product': product,
        'category': category,
        'brand': brand ,
    
    }
    return render(request,'store.html', context)


def product(request, id):
    product = get_object_or_404(Product,id=id)
    category = Category.objects.all()
    brand = Brand.objects.all()


    context = {
        'product': product,
        'category': category,
        'brand ': brand ,
    }
    
    return render(request,'product.html',context)


def checkout(request):
    return render(request,'checkout.html',)


def blank(request):
    return render(request,'blank.html',)









