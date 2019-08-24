"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.main, name='home'),
    path('contacts/', mainapp.contacts, name='contacts'),
    path('products/all/', mainapp.products, name='products'),

    path('products/all', mainapp.products, name='ALL'),
    path('products/home', mainapp.products, name='HOME'),
    path('products/office', mainapp.products, name='OFFICE'),
    path('products/furniture', mainapp.products, name='FURNITURE'),
    path('products/modern', mainapp.products, name='MODERN'),
    path('products/classic', mainapp.products, name='CLASSIC'),

    path('product/', mainapp.product, name='product'),
]
