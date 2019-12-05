from django.utils.translation import ugettext_lazy as _
from django.db import models

class UserRoleChoice(models.IntegerChoices):
  SUPERADMIN = 1
  ADMIN = 2
  PROVIDER = 3
  CUSTOMER = 4