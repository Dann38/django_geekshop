from django.shortcuts import render
from .models import Product

# Create your views here.
MENU = [
    {'href': 'mainapp:main', 'name': 'home'},
    {'href': 'mainapp:products_url:products', 'name': 'products'},
    {'href': 'mainapp:contacts', 'name': 'contacts'},
]

# product_type = [
#     {'href': 'products_url:all', 'name': 'all'},
#     {'href': 'products_url:home', 'name': 'home'},
#     {'href': 'products_url:office', 'name': 'office'},
#     {'href': 'products_url:furniture', 'name': 'furniture'},
#     {'href': 'products_url:modern', 'name': 'modern'},
#     {'href': 'products_url:classic', 'name': 'classic'},
# ]

products = Product.objects
PRODUCT_WITHOUT_MARK = products.filter(mark='')
PRODUCT_EXCLUSIVE = products.filter(mark='exclusive')
PRODUCT_TRENDING = products.filter(mark='trending')

def main(request):
    products_shelf2 = PRODUCT_WITHOUT_MARK[:4]
    products_exclusive = PRODUCT_EXCLUSIVE[:2]
    products_trending = PRODUCT_TRENDING[:6]
    products_shelf6_max = PRODUCT_WITHOUT_MARK[4:5]
    products_shelf6_min = PRODUCT_WITHOUT_MARK[:4]

    context = {
        'title':'Главная',
        "list_menu": MENU,
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
        "list_menu": MENU,
    }
    return render(request, 'mainapp/contacts.html', context=context)


def products(request):
    context = {
        'title': 'Продукты',
        "list_menu": MENU,
        # 'product_list_menu': product_type
    }
    return render(request, 'mainapp/products.html', context=context)


def product(request):
    context = {
        'title': 'Продукт',
        "list_menu": MENU,
        # 'product_list_menu': product_type
    }
    return render(request, 'mainapp/product.html', context=context)