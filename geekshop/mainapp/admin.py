from django.contrib import admin
from .models import Product, CategoryProducts

admin.site.register(Product)
admin.site.register(CategoryProducts)

