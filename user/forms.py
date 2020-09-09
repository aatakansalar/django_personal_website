from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı adı")
    password = forms.CharField(label = "Şifre", widget = forms.PasswordInput)