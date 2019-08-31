from django.urls import include, path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/', include('mainapp.urls', namespace='products_url')),

    path('product/', views.product, name='product'),

]