from django.db import models
from django.utils.translation import ugettext_lazy as _

class CategoryStatus(models.IntegerChoices):
  PUBLISHED = 1
  UNPUBLISHED = 2