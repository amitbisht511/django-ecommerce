from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from categories.models import Category

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(verbose_name=_('Describe products'))
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='products/')
    quantity = models.IntegerField(verbose_name=_('Quantity of products'))
    price = models.FloatField(verbose_name=_('Price of product'))
    category = models.ForeignKey(
        Category, related_name='category_products', on_delete=models.CASCADE)
    provider = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def is_available(self):
        return self.quantity >= 1
