from django.shortcuts import get_object_or_404, render
from authapp.models import ShopUser
from ..mainapp.models import Product, CategoryProducts



def users(request):
    title = 'админка/пользователя'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'objects': users_list,
    }

    return render(request, 'adminapp/users.html', context)

def user_create(request):
    pass


def user_update(request, pk):
    pass


def user_delete(request, pk):
    pass




def categories(request):
    title = 'админка/категории'

    categories_list = CategoryProducts.objects.all()

    context = {
        'title': title,
        'objects': categories_list,
    }

    return render(request, 'adminapp/categories.html', context)


def category_create(request):
    pass


def category_update(request, pk):
    pass


def category_delete(request, pk):
    pass




def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(CategoryProducts, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context={
        'title': title,
        'category': category,
        'objects': products_list
    }

    return render(request, 'adminapp/products.html', context)

def product_create(request, pk):
    pass

def product_read(request, pk):
    pass

def product_update(request, pk):
    pass

def product_delete(request, pk):
    pass

