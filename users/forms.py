from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

# Register your models here.
class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('email',  )

class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = User
    fields = 'email', 'password', 'first_name', 'last_name', 'age', 'is_active'