from django.db import models
from django.utils.translation import ugettext_lazy as _
from .choices import CategoryStatus
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(verbose_name=_('Describe about Category'))
    parent_category = models.ForeignKey('self',  on_delete=models.CASCADE, null=True, blank=True)
    status = models.IntegerField(
        choices=CategoryStatus.choices, default=CategoryStatus.UNPUBLISHED)

    def __str__(self):
        return self.title

    @property
    def is_published(self):
        return self.status == CategoryStatus.PUBLISHED
