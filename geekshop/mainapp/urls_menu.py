from django.urls import include, path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/', include('mainapp.urls_menu_products', namespace='products_url')),

    path('product/', views.product, name='product'),

]