from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': "form-control", 'placeholder': "Create password", 'autocomplete': "off", 'type': "password",
               'id': "password"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': "form-control", 'placeholder': "Your email", 'autocomplete': "off", 'type': "email",
               'id': "email"}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Your username", 'autocomplete': "off", 'type': "text",
               'id': "username"}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class LoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': "form-control", 'placeholder': "Password", 'autocomplete': "off", 'id': "password",
               "type": "password"}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Your username", 'autocomplete': "off", 'type': "text",
               'id': "username"}))
