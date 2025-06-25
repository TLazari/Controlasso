"""
Testes para os modelos do aplicativo core.

Testa todos os modelos incluindo validações, métodos personalizados,
relacionamentos e cenários de erro.
"""

import pytest
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from decimal import Decimal
from core.models import Account, Transfer, Stock, Trade, FavoriteStock

User = get_user_model()

@pytest.mark.django_db
class TestTransferModel:
    """Testes para o modelo Transfer."""

    def test_criacao_transferencia(self, user, another_user, transfer_factory):
        """Testa a criação de uma transferência."""
        transfer = transfer_factory(
            sender=user,
            recipient=another_user,
            amount=100.00
        )
        
        assert transfer.id is not None
        assert transfer.sender == user
        assert transfer.recipient == another_user
        assert transfer.amount == Decimal('100.00')
        assert transfer.created_at is not None

    def test_relacionamentos_com_user(self, user, another_user, transfer_factory):
        """Testa os relacionamentos com o modelo User."""
        transfer = transfer_factory(
            sender=user,
            recipient=another_user,
            amount=100.00
        )
        
        assert transfer in user.sent_transfers.all()
        assert transfer in another_user.received_transfers.all()


@pytest.mark.django_db
class TestStockModel:
    """Testes para o modelo Stock."""

    def test_criacao_stock(self, stock_factory):
        """Testa a criação de uma ação."""
        stock = stock_factory(
            name='Microsoft Corporation',
            code='MSFT',
            current_price=300.50
        )
        
        assert stock.id is not None
        assert stock.name == 'Microsoft Corporation'
        assert stock.code == 'MSFT'
        assert stock.current_price == Decimal('300.50')


    def test_atualizacao_preco(self, stock):
        """Testa a atualização do preço da ação."""
        novo_preco = Decimal('175.25')
        stock.current_price = novo_preco
        stock.save()
        
        stock.refresh_from_db()
        assert stock.current_price == novo_preco


@pytest.mark.django_db
class TestTradeModel:
    """Testes para o modelo Trade."""

    def test_criacao_trade_compra(self, user, stock, trade_factory):
        """Testa a criação de uma operação de compra."""
        trade = trade_factory(
            user=user,
            stock=stock,
            quantity=50,
            trade_type='buy',
            price=120.00
        )
        
        assert trade.id is not None
        assert trade.user == user
        assert trade.stock == stock
        assert trade.quantity == 50
        assert trade.trade_type == 'buy'
        assert trade.price == Decimal('120.00')
        assert trade.created_at is not None

    def test_str_representacao(self, user, stock, trade_factory):
        """Testa a representação string do modelo Trade."""
        trade = trade_factory(
            user=user,
            stock=stock,
            quantity=25,
            trade_type='buy',
            price=90.00
        )
        
        expected = f"Compra 25 {stock.code}"
        assert str(trade) == expected

    def test_choices_trade_type(self):
        """Testa as opções de tipo de operação."""
        assert Trade.BUY == "buy"
        assert Trade.SELL == "sell"
        assert len(Trade.TYPE_CHOICES) == 2


@pytest.mark.django_db
class TestFavoriteStockModel:
    """Testes para o modelo FavoriteStock."""

    def test_criacao_favorito(self, user, stock, favorite_stock_factory):
        """Testa a criação de uma ação favorita."""
        favorite = favorite_stock_factory(user=user, stock=stock)
        
        assert favorite.id is not None
        assert favorite.user == user
        assert favorite.stock == stock

    def test_unique_together_constraint(self, user, stock):
        """Testa a restrição unique_together."""
        # Criar o primeiro favorito
        FavoriteStock.objects.create(user=user, stock=stock)
        
        # Tentar criar um favorito duplicado deve falhar
        with pytest.raises(IntegrityError):
            FavoriteStock.objects.create(user=user, stock=stock)

    def test_multiplos_usuarios_mesma_acao(self, user_factory, stock, favorite_stock_factory):
        """Testa que múltiplos usuários podem favoritar a mesma ação."""
        user1 = user_factory()
        user2 = user_factory()
        
        favorite1 = favorite_stock_factory(user=user1, stock=stock)
        favorite2 = favorite_stock_factory(user=user2, stock=stock)
        
        assert favorite1.id != favorite2.id
        assert favorite1.stock == favorite2.stock

    def test_usuario_multiplas_acoes_favoritas(self, user, stock_factory, favorite_stock_factory):
        """Testa que um usuário pode ter múltiplas ações favoritas."""
        stock1 = stock_factory(code='GOOG')
        stock2 = stock_factory(code='TSLA')
        
        favorite1 = favorite_stock_factory(user=user, stock=stock1)
        favorite2 = favorite_stock_factory(user=user, stock=stock2)
        
        assert favorite1.id != favorite2.id
        assert favorite1.user == favorite2.user