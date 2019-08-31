from django.shortcuts import render
from .models import Product

# Create your views here.
menu = [
    {'href': 'main', 'name': 'home'},
    {'href': 'products', 'name': 'products'},
    {'href': 'contacts', 'name': 'contacts'},
]

product_type = [
    {'href': 'all', 'name': 'all'},
    {'href': 'home', 'name': 'home'},
    {'href': 'office', 'name': 'office'},
    {'href': 'furniture', 'name': 'furniture'},
    {'href': 'modern', 'name': 'modern'},
    {'href': 'classic', 'name': 'classic'},
]

def main(request):
    products = Product.objects
    products_shelf2 = products.filter(mark='')[:4]
    products_exclusive = products.filter(mark='exclusive')[:2]
    products_trending = products.filter(mark='trending')[:6]
    products_shelf6_max = products.filter(mark='')[4:5]
    products_shelf6_min = products.filter(mark='')[5:9]


    context = {
        'title':'Главная',
        "list_menu": menu,
        'products_shelf2': products_shelf2,
        'products_exclusive': products_exclusive,
        'products_trending': products_trending,
        'products_shelf6_max': products_shelf6_max,
        'products_shelf6_min': products_shelf6_min,
    }

    return render(request, 'mainapp/index.html', context=context)


def contacts(request):
    context = {
        'title': 'Контакты',
        "list_menu": menu,
    }
    return render(request, 'mainapp/contacts.html', context=context)


def products(request):
    context = {
        'title': 'Продукты',
        "list_menu": menu,
        'product_list_menu': product_type
    }
    return render(request, 'mainapp/products.html', context=context)


def product(request):
    context = {
        'title': 'Продукт',
        "list_menu": menu,
        'product_list_menu': product_type
    }
    return render(request, 'mainapp/product.html', context=context)