
from django.contrib import admin

from .models import Account, FavoriteStock, Stock, Trade, Transfer

"""
Configuração do Django Admin para o projeto.

Registra os modelos principais para serem gerenciados pela interface administrativa do Django.

Modelos registrados:
    - Account: Representa contas de usuário no sistema.
    - Transfer: Registra transferências financeiras entre contas.
    - Stock: Representa ações disponíveis para negociação.
    - Trade: Histórico e operações de compra e venda de ações.
    - FavoriteStock: Marcações de ações favoritas por usuários.
"""

admin.site.register(Account)
admin.site.register(Transfer)
admin.site.register(Stock)
admin.site.register(Trade)
admin.site.register(FavoriteStock)