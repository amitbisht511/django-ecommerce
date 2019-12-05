from django.contrib.auth.models import BaseUserManager
from .choices import UserRoleChoice


class CustomUserManager(BaseUserManager):
    """
    Custom User Manager
    """

    def create_user(self, email, first_name, last_name, password=None, **kwargs):
        if not email:
            raise ValueError('Email Must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_super_user(self, email, first_name, last_name, password=None, **kwargs):
        kwargs.setdefault('role', UserRoleChoice.SUPERADMIN)
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('email_verified', True)
        self.create_user(email, password, first_name, last_name, **kwargs)
