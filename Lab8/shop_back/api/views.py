
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from api.models import *

def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values())}
    return JsonResponse(data)

def product_detail(request, id):
    product = render(Product, id=id)
    data = {"products":{
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "count":product.count,
        "is_active":product.is_active
    }}
    return JsonResponse(data)

def category_list(request):
    categories = Category.objects.all()
    data ={"catageries": list(categories.values())}
    return JsonResponse(data)

def category_detail(request, id):
    category = render(Category, id=id)
    data = { "category": {
        "name": category.name,
    }}
    return JsonResponse(data)

def category_products(request, id):
    category = render(Category, id=id)
    products = category.product_set.all()
    data= {"products" : list(products.values())}
    return JsonResponse(data)