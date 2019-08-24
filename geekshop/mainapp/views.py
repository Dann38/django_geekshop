from django.shortcuts import render

# Create your views here.
menu = [
    {'href': '/', 'name': 'home'},
    {'href': '/products/all', 'name': 'products'},
    {'href': '/contacts', 'name': 'contacts'},
]

def main(request):
    context = {
        'title':'Главная',
        "list_menu": menu,
    }
    return render(request, 'mainapp/index.html', context=context)


def contacts(request):
    context = {
        'title': 'Контакты',
        "list_menu": menu,
    }
    return render(request, 'mainapp/contacts.html', context=context)


def products(request):
    product_type = [
        {'href': '/products/all', 'name': 'ALL'},
        {'href': '/products/home', 'name': 'HOME'},
        {'href': '/products/office', 'name': 'OFFICE'},
        {'href': '/products/furniture', 'name': 'FURNITURE'},
        {'href': '/products/modern', 'name': 'MODERN'},
        {'href': '/products/classic', 'name': 'CLASSIC'},
    ]

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
    }
    return render(request, 'mainapp/product.html', context=context)