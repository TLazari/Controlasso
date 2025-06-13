from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Nome de Usuário")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
