from django.shortcuts import render

# Create your views here.
menu = [
    {'href': '/', 'name': 'home'},
    {'href': '/products', 'name': 'products'},
    {'href': '/contacts', 'name': 'contacts'},
]
def main(request):
    context = {
        'title':'/',
        "list_menu": menu,
    }
    return render(request, 'mainapp/index.html', context=context)


def contacts(request):
    context = {
        'title': '/contacts',
        "list_menu": menu,
    }
    return render(request, 'mainapp/contacts.html', context=context)


def products(request):
    context = {
        'title': '/products',
        "list_menu": menu,
    }
    return render(request, 'mainapp/products.html', context=context)


def product(request):
    context = {
        'title': '/product',
        "list_menu": menu,
    }
    return render(request, 'mainapp/product.html', context=context)