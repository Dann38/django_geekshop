from django.core.management.base import BaseCommand
from mainapp.models import CategoryProducts, Product
from django.contrib.auth.models import User
from authapp.models import ShopUser

import json, os

JSON_PATH = 'mainapp/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        CategoryProducts.objects.all().delete()
        for ctg in categories:
            new_ctg = CategoryProducts(**ctg)
            new_ctg.save()

        products =load_from_json('products')

        Product.objects.all().delete()
        for prd in products:
            ctg_name = prd['category']
            _ctg = CategoryProducts.objects.get(name=ctg_name)
            prd['category'] = _ctg
            new_prd = Product(**prd)
            new_prd.save()

        super_user = ShopUser.objects.create_superuser('django',
                                                   'django@geekshop.local',
                                                   'geekbrains', age=33)

