from django.db import models

class CategoryProducts(models.Model):
    name = models.CharField(verbose_name='имя категории', max_length=128, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128, unique=True)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(verbose_name='описание товара', blank=True)
    min_des = models.TextField(verbose_name='краткое описание', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='кол-во', default=0)
    mark = models.CharField(verbose_name='маркер', max_length=128, blank=True)


    def __str__(self):
        return f'{self.name}({self.category.name})'
