from django.urls import path
from . import views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='products'),

    path('all', mainapp.products, name='all'),
    path('home', mainapp.products, name='home'),
    path('office', mainapp.products, name='office'),
    path('furniture', mainapp.products, name='furniture'),
    path('modern', mainapp.products, name='modern'),
    path('classic', mainapp.products, name='classic'),


]
