from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = 'email', 'first_name', 'last_name', 'is_active', 'role', 'last_login'
    list_filter = 'is_active', 'role'
    fieldsets = (
      ('None', {'fields': ('email', 'password')}),
      ('Information',{'fields':('first_name', 'last_name', 'age')}),
      ('Permissions', {'fields':('is_active', 'role')})
    )
    add_fieldsets = (
      ('None', {
        'classes':('wide',),
        'fields':('email', 'password1', 'password2')
      }),(
        'Information', {
          'classes':('wide',),
          'fields':('first_name', 'last_name', 'age')
        }
      ),(
        'Permissions', {
          'fields':('is_active', 'role')
        }
      )
    )
    search_fields = 'email', 'first_name', 'last_name'
    ordering = 'first_name', 'email'

admin.site.register(User, CustomUserAdmin)