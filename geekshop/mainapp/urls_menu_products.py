from django.urls import path
from . import views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='products'),
    path('<int:pk>/', mainapp.products, name='category')


]
