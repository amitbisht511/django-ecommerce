from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from .choices import UserRoleChoice
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(max_length=255, unique=True, verbose_name=_('Email Address'))
  role = models.IntegerField(choices=UserRoleChoice.choices)
  is_active = models.BooleanField(verbose_name=_('Is Active User'), default=True)
  email_verified = models.BooleanField(verbose_name=_('Email Verified ?'), default=False)
  first_name = models.CharField(verbose_name=_('First Name'), max_length=255)
  last_name = models.CharField(verbose_name=_('Last Name'), max_length=255, null=True, blank=True)
  age = models.IntegerField(verbose_name=_('Age'), null=True, blank=True)
  last_login = models.DateTimeField(verbose_name=_('Last Login'), auto_now_add=True)
  date_joined = models.DateTimeField(verbose_name=_('Date Joined'), auto_now_add=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  objects = CustomUserManager()


  def __str__(self):
    return self.email
  
  def get_full_name(self):
    return self.first_name+' '+self.last_name

  def get_short_name(self):
    return self.first_name
  
  @property
  def is_staff(self):
    return True
