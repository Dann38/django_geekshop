from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'mainapp/index.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def products(request):
    return render(request, 'mainapp/products.html')


def product(request):
    return render(request, 'mainapp/product.html')