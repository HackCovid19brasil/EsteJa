from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import CustomUser

class CustomUserForm(ModelForm):
  class Meta:
    model = CustomUser
    exclude = ['user', 'approved']
