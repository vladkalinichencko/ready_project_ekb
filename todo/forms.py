from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "mailField", 'placeholder': 'Твоя электропочта'}) ,label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "passwordField", 'placeholder': 'Твой пароль'}) ,label='')