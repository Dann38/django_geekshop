from django.urls import path
from . import views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='products'),

    path('all', mainapp.products, name='all'),
    path('products/home', mainapp.products, name='home'),
    path('products/office', mainapp.products, name='office'),
    path('products/furniture', mainapp.products, name='furniture'),
    path('products/modern', mainapp.products, name='modern'),
    path('products/classic', mainapp.products, name='classic'),


]
