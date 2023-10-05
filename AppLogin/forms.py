from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email Address', required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'autofocus':True
    }))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
class ProfileChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
class ProfilePic(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ('profilepic',)