from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        required=True,
        label="Senha",
        widget=forms.PasswordInput,  # <- Adicione este widget
    )

    password2 = forms.CharField(
        required=True,
        label="Repita a senha",
        widget=forms.PasswordInput,  # <- Adicione este widget
    )
    email = forms.EmailField(required=True, label="E-mail")

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]

        labels = {
            "username": "Nome de Usuário",
        }

    def clean_email(self):
        email = self.cleaned_data.get("email", "").strip().lower()
        if not email:
            raise ValidationError("O campo e-mail é obrigatório.", code="required")

        exists = User.objects.filter(email__iexact=email).exists()
        if exists:
            raise ValidationError("Este e-mail já está em uso", code="invalid")
        return email

    def clean_first_name(self):
        data = self.cleaned_data.get("first_name")

        if data and "admin" in data:
            raise ValidationError(
                "Seu nome não pode ser %(value)s",
                code="invalid",
                params={"value": '"admin"'},
            )

        return data

    def clean_username(self):
        data = self.cleaned_data.get("username")

        if data and "admin" in data:
            raise ValidationError(
                "Seu nome de usuario não pode ser %(value)s",
                code="invalid",
                params={"value": '"admin"'},
            )

        return data

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            password_confirmation_error = ValidationError("As senhas não conferem", code="invalid")
            raise ValidationError(
                {
                    "password2": [
                        password_confirmation_error,
                    ],
                }
            )
        return cleaned_data
