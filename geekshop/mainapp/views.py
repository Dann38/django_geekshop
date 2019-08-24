from django.shortcuts import render

# Create your views here.
menu = [
    {'href': 'main', 'name': 'home'},
    {'href': 'products', 'name': 'products'},
    {'href': 'contacts', 'name': 'contacts'},
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
        {'href': 'all', 'name': 'all'},
        {'href': 'home', 'name': 'home'},
        {'href': 'office', 'name': 'office'},
        {'href': 'furniture', 'name': 'furniture'},
        {'href': 'modern', 'name': 'modern'},
        {'href': 'classic', 'name': 'classic'},
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