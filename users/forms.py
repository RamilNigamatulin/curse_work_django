from users.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from catalog.forms import StyleFormMixin


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)
        #fields = '__all__'
        #exclude = ('',)
