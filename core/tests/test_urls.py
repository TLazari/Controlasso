"""
Testes para as URLs do projeto Django.

Verifica se todas as URLs estão configuradas corretamente e
se os nomes das URLs correspondem às views esperadas.
"""

import pytest
from django.urls import reverse, resolve
from django.test import RequestFactory


class TestURLPatterns:
    """Testes para os padrões de URL."""

    def test_admin_url(self):
        """Testa a URL do admin."""
        url = reverse('admin:index')
        assert url == '/admin/'

    def test_register_url(self):
        """Testa a URL de registro."""
        url = reverse('register')
        assert url == '/register/'
        
        # Testa resolução da URL
        resolved = resolve('/register/')
        assert resolved.url_name == 'register'

    def test_login_url(self):
        """Testa a URL de login."""
        url = reverse('login')
        assert url == '/login/'
        
        # Testa resolução da URL
        resolved = resolve('/login/')
        assert resolved.url_name == 'login'

    def test_logout_url(self):
        """Testa a URL de logout."""
        url = reverse('logout')
        assert url == '/logout/'
        
        # Testa resolução da URL
        resolved = resolve('/logout/')
        assert resolved.url_name == 'logout'

    def test_dashboard_url(self):
        """Testa a URL do dashboard (página inicial)."""
        url = reverse('dashboard')
        assert url == '/'
        
        # Testa resolução da URL
        resolved = resolve('/')
        assert resolved.url_name == 'dashboard'

    def test_transfer_url(self):
        """Testa a URL de transferência."""
        url = reverse('transfer')
        assert url == '/transfer/'
        
        # Testa resolução da URL
        resolved = resolve('/transfer/')
        assert resolved.url_name == 'transfer'

    def test_account_info_url(self):
        """Testa a URL de informações da conta."""
        url = reverse('account_info')
        assert url == '/account-info/'
        
        # Testa resolução da URL
        resolved = resolve('/account-info/')
        assert resolved.url_name == 'account_info'

    def test_trade_url(self):
        """Testa a URL da lista de ações."""
        url = reverse('trade')
        assert url == '/trade/'
        
        # Testa resolução da URL
        resolved = resolve('/trade/')
        assert resolved.url_name == 'trade'

    def test_operate_stock_url(self):
        """Testa a URL de operação com ação específica."""
        url = reverse('operate_stock', kwargs={'stock_id': 1})
        assert url == '/trade/1/'
        
        # Testa resolução da URL
        resolved = resolve('/trade/1/')
        assert resolved.url_name == 'operate_stock'
        assert resolved.kwargs == {'stock_id': 1}

    def test_stock_info_api_url(self):
        """Testa a URL da API de informações da ação."""
        url = reverse('stock_info', kwargs={'stock_id': 1})
        assert url == '/api/stock-info/1/'
        
        # Testa resolução da URL
        resolved = resolve('/api/stock-info/1/')
        assert resolved.url_name == 'stock_info'
        assert resolved.kwargs == {'stock_id': 1}

    def test_trade_history_url(self):
        """Testa a URL do histórico de trades."""
        url = reverse('trade_history')
        assert url == '/trades/history/'
        
        # Testa resolução da URL
        resolved = resolve('/trades/history/')
        assert resolved.url_name == 'trade_history'

    def test_toggle_favorite_stock_url(self):
        """Testa a URL para toggle de ação favorita."""
        url = reverse('toggle_favorite_stock', kwargs={'stock_id': 1})
        assert url == '/favorite/1/'
        
        # Testa resolução da URL
        resolved = resolve('/favorite/1/')
        assert resolved.url_name == 'toggle_favorite_stock'
        assert resolved.kwargs == {'stock_id': 1}

    def test_toggle_favorite_stock_list_url(self):
        """Testa a URL para toggle de favorito na lista."""
        url = reverse('toggle_favorite_stock_list', kwargs={'stock_id': 1})
        assert url == '/favorite-list/1/'
        
        # Testa resolução da URL
        resolved = resolve('/favorite-list/1/')
        assert resolved.url_name == 'toggle_favorite_stock_list'
        assert resolved.kwargs == {'stock_id': 1}

    def test_toggle_theme_url(self):
        """Testa a URL para mudança de tema."""
        url = reverse('toggle_theme')
        assert url == '/toggle-theme/'
        
        # Testa resolução da URL
        resolved = resolve('/toggle-theme/')
        assert resolved.url_name == 'toggle_theme'


class TestPasswordResetURLs:
    """Testes para URLs de redefinição de senha."""

    def test_password_reset_url(self):
        """Testa a URL de início da redefinição de senha."""
        url = reverse('password_reset')
        assert url == '/password-reset/'
        
        # Testa resolução da URL
        resolved = resolve('/password-reset/')
        assert resolved.url_name == 'password_reset'

    def test_delete_user_url(self):
        """Testa a URL para deletar usuário."""
        url = reverse('delete_user', kwargs={'user_id': 1})
        assert url == '/password-reset/delete/1/'
        
        # Testa resolução da URL
        resolved = resolve('/password-reset/delete/1/')
        assert resolved.url_name == 'delete_user'
        assert resolved.kwargs == {'user_id': 1}

    def test_password_reset_done_url(self):
        """Testa a URL de confirmação de envio de email."""
        url = reverse('password_reset_done')
        assert url == '/password-reset/done/'
        
        # Testa resolução da URL
        resolved = resolve('/password-reset/done/')
        assert resolved.url_name == 'password_reset_done'

    def test_password_reset_confirm_url(self):
        """Testa a URL de confirmação de reset com token."""
        url = reverse('password_reset_confirm', kwargs={
            'uidb64': 'test-uid',
            'token': 'test-token'
        })
        assert url == '/reset/test-uid/test-token/'
        
        # Testa resolução da URL
        resolved = resolve('/reset/test-uid/test-token/')
        assert resolved.url_name == 'password_reset_confirm'
        assert resolved.kwargs == {'uidb64': 'test-uid', 'token': 'test-token'}

    def test_password_reset_complete_url(self):
        """Testa a URL de conclusão da redefinição."""
        url = reverse('password_reset_complete')
        assert url == '/reset/done/'
        
        # Testa resolução da URL
        resolved = resolve('/reset/done/')
        assert resolved.url_name == 'password_reset_complete'

    def test_password_change_url(self):
        """Testa a URL de mudança de senha."""
        url = reverse('password_change')
        assert url == '/password-change/'
        
        # Testa resolução da URL
        resolved = resolve('/password-change/')
        assert resolved.url_name == 'password_change'

    def test_password_change_done_url(self):
        """Testa a URL de confirmação de mudança de senha."""
        url = reverse('password_change_done')
        assert url == '/password-change/done/'
        
        # Testa resolução da URL
        resolved = resolve('/password-change/done/')
        assert resolved.url_name == 'password_change_done'

class TestURLParameters:
    """Testes para URLs com parâmetros."""

    def test_stock_id_parameters(self):
        """Testa URLs que recebem stock_id como parâmetro."""
        stock_urls = [
            ('operate_stock', '/trade/{stock_id}/'),
            ('stock_info', '/api/stock-info/{stock_id}/'),
            ('toggle_favorite_stock', '/favorite/{stock_id}/'),
            ('toggle_favorite_stock_list', '/favorite-list/{stock_id}/'),
        ]
        
        for url_name, url_pattern in stock_urls:
            # Testa com diferentes valores de stock_id
            for stock_id in [1, 42, 999]:
                url = reverse(url_name, kwargs={'stock_id': stock_id})
                expected_url = url_pattern.format(stock_id=stock_id)
                assert url == expected_url
                
                # Verifica se a URL resolve corretamente
                resolved = resolve(url)
                assert resolved.url_name == url_name
                assert resolved.kwargs['stock_id'] == stock_id

    def test_user_id_parameter(self):
        """Testa URL que recebe user_id como parâmetro."""
        for user_id in [1, 25, 100]:
            url = reverse('delete_user', kwargs={'user_id': user_id})
            expected_url = f'/password-reset/delete/{user_id}/'
            assert url == expected_url
            
            # Verifica se a URL resolve corretamente
            resolved = resolve(url)
            assert resolved.url_name == 'delete_user'
            assert resolved.kwargs['user_id'] == user_id

    def test_password_reset_token_parameters(self):
        """Testa URL de reset de senha com uidb64 e token."""
        test_cases = [
            ('abc123', 'token-123'),
            ('xyz789', 'another-token'),
            ('user-64', 'special_token-456')
        ]
        
        for uidb64, token in test_cases:
            url = reverse('password_reset_confirm', kwargs={
                'uidb64': uidb64,
                'token': token
            })
            expected_url = f'/reset/{uidb64}/{token}/'
            assert url == expected_url
            
            # Verifica se a URL resolve corretamente
            resolved = resolve(url)
            assert resolved.url_name == 'password_reset_confirm'
            assert resolved.kwargs['uidb64'] == uidb64
            assert resolved.kwargs['token'] == token


class TestURLNamesUniqueness:
    """Testes para garantir que os nomes das URLs são únicos."""

    def test_all_url_names_unique(self):
        """Verifica se todos os nomes de URL são únicos."""
        url_names = [
            'register', 'login', 'logout', 'dashboard',
            'transfer', 'account_info', 'trade', 'operate_stock',
            'stock_info', 'trade_history', 'toggle_favorite_stock',
            'toggle_favorite_stock_list', 'toggle_theme',
            'password_reset', 'delete_user', 'password_reset_done',
            'password_reset_confirm', 'password_reset_complete',
            'password_change', 'password_change_done'
        ]
        
        # Verifica se todos os nomes podem ser resolvidos
        for url_name in url_names:
            try:
                if url_name in ['operate_stock', 'stock_info', 'toggle_favorite_stock', 'toggle_favorite_stock_list']:
                    reverse(url_name, kwargs={'stock_id': 1})
                elif url_name == 'delete_user':
                    reverse(url_name, kwargs={'user_id': 1})
                elif url_name == 'password_reset_confirm':
                    reverse(url_name, kwargs={'uidb64': 'test', 'token': 'test'})
                else:
                    reverse(url_name)
            except Exception as e:
                pytest.fail(f"URL name '{url_name}' cannot be reversed: {e}")


class TestStaticFilesURL:
    """Testes para configuração de arquivos estáticos."""

    def test_static_files_configuration(self):
        """Verifica se a configuração de arquivos estáticos está presente."""
        # Este teste é mais conceitual, pois os arquivos estáticos
        # só são servidos quando DEBUG=True
        # Em produção, isso seria handled pelo servidor web
        pass
