from django import forms
from django.contrib.auth.forms import UserCreationForm
import sys
sys.path.insert(1, 'SEProject/users')
from users.models import CustomUser

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')