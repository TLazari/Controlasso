"""
Configurações e fixtures do pytest para o projeto Django.

Este arquivo contém as configurações gerais do pytest e fixtures
reutilizáveis para os testes do projeto.
"""

import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from core.models import Account, Stock, Transfer, Trade, FavoriteStock
import uuid
from decimal import Decimal

User = get_user_model()


@pytest.fixture(scope='session')
def django_db_setup():
    """Configuração da base de dados para os testes."""
    pass


@pytest.fixture
def client():
    """Cliente de testes do Django."""
    return Client()


@pytest.fixture
def user_factory():
    """Factory para criar usuários únicos."""
    def _create_user(username=None, email=None, password='testpass123'):
        if username is None:
            username = f'testuser_{uuid.uuid4().hex[:8]}'
        if email is None:
            email = f'{username}@test.com'
        return User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
    return _create_user


@pytest.fixture
def user(user_factory):
    """Usuário de teste padrão."""
    return user_factory()


@pytest.fixture
def another_user(user_factory):
    """Segundo usuário para testes de transferência."""
    return user_factory(username='anotheruser')


@pytest.fixture
def account_factory(user_factory):
    """Factory para criar contas."""
    def _create_account(user=None, balance=1000.00, theme='light'):
        if user is None:
            user = user_factory()
        
        account_number = f'{uuid.uuid4().hex[:5]}'
        return Account.objects.create(
            user=user,
            account_number=account_number,
            balance=Decimal(str(balance)),
            theme=theme
        )
    return _create_account


@pytest.fixture
def account(account_factory, user):
    """Conta de teste padrão."""
    return account_factory(user=user)


@pytest.fixture
def another_account(account_factory, another_user):
    """Segunda conta para testes de transferência."""
    return account_factory(user=another_user, balance=500.00)


@pytest.fixture
def stock_factory():
    """Factory para criar ações."""
    def _create_stock(name=None, code=None, current_price=100.00):
        if name is None:
            name = f'Empresa {uuid.uuid4().hex[:8]}'
        if code is None:
            code = f'TEST{uuid.uuid4().hex[:3].upper()}'
        
        return Stock.objects.create(
            name=name,
            code=code,
            current_price=Decimal(str(current_price))
        )
    return _create_stock


@pytest.fixture
def stock(stock_factory):
    """Ação de teste padrão."""
    return stock_factory(name='Apple Inc.', code='AAPL', current_price=150.00)


@pytest.fixture
def transfer_factory():
    """Factory para criar transferências."""
    def _create_transfer(sender, recipient, amount):
        return Transfer.objects.create(
            sender=sender,
            recipient=recipient,
            amount=Decimal(str(amount))
        )
    return _create_transfer


@pytest.fixture
def trade_factory():
    """Factory para criar operações de trade."""
    def _create_trade(user, stock, quantity=10, trade_type='buy', price=100.00):
        return Trade.objects.create(
            user=user,
            stock=stock,
            quantity=quantity,
            trade_type=trade_type,
            price=Decimal(str(price))
        )
    return _create_trade


@pytest.fixture
def authenticated_client(client, user):
    """Cliente autenticado com usuário de teste."""
    client.force_login(user)
    return client


@pytest.fixture
def favorite_stock_factory():
    """Factory para criar ações favoritas."""
    def _create_favorite(user, stock):
        return FavoriteStock.objects.create(user=user, stock=stock)
    return _create_favorite