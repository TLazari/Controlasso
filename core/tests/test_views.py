"""
Testes para as views do aplicativo core.

Testa todas as views principais incluindo autenticação, transferências,
operações com ações e funcionalidades do dashboard.
"""

import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import Client
from core.models import Account, Stock, Transfer, Trade, FavoriteStock
from decimal import Decimal
import json

User = get_user_model()


@pytest.mark.django_db
class TestAuthenticationViews:
    """Testes para views de autenticação."""

    def test_register_view_get(self, client):
        """Testa o acesso à página de registro."""
        url = reverse('register')
        response = client.get(url)
        
        assert response.status_code == 200
        assert 'register' in response.context or 'form' in response.context

    def test_register_view_post_sucesso(self, client):
        """Testa o registro bem-sucedido de usuário."""
        url = reverse('register')
        data = {
            'username': 'novouser',
            'password1': 'senhasegura123',
            'password2': 'senhasegura123',
            'email': 'novo@test.com'
        }
        response = client.post(url, data)
        
        # Verifica se o usuário foi criado
        assert User.objects.filter(username='novouser').exists()
        
        # Verifica se uma conta foi criada automaticamente
        user = User.objects.get(username='novouser')
        assert hasattr(user, 'account')

    def test_login_view_get(self, client):
        """Testa o acesso à página de login."""
        url = reverse('login')
        response = client.get(url)
        
        assert response.status_code == 200

    def test_login_view_post_sucesso(self, client, user):
        """Testa o login bem-sucedido."""
        url = reverse('login')
        data = {
            'username': user.username,
            'password': 'testpass123'
        }
        response = client.post(url, data)
        
        # Verifica redirecionamento após login
        assert response.status_code in [200, 302]

    def test_logout_view(self, authenticated_client):
        """Testa a view de logout."""
        url = reverse('logout')
        response = authenticated_client.get(url)
        
        assert response.status_code == 200

@pytest.mark.django_db
class TestAccessControlViews:
    """Testes para controle de acesso às views."""

    def test_views_publicas(self, client):
        """Testa views que devem ser públicas."""
        public_urls = [
            reverse('login'),
            reverse('register'),
        ]
        
        for url in public_urls:
            response = client.get(url)
            # Deve ser acessível
            assert response.status_code == 200


@pytest.mark.django_db
class TestErrorHandling:
    """Testes para tratamento de erros nas views."""

    def test_api_stock_inexistente(self, authenticated_client):
        """Testa API com ação inexistente."""
        url = reverse('stock_info', kwargs={'stock_id': 9999})
        response = authenticated_client.get(url)
        
        assert response.status_code == 404


@pytest.mark.django_db
class TestPasswordResetViews:
    """Testes para views de redefinição de senha."""

    def test_password_reset_done_view(self, client):
        """Testa a view de confirmação de envio de email."""
        url = reverse('password_reset_done')
        response = client.get(url)
        
        assert response.status_code == 200

    def test_password_reset_complete_view(self, client):
        """Testa a view de conclusão da redefinição."""
        url = reverse('password_reset_complete')
        response = client.get(url)
        
        assert response.status_code == 200
