from django.db import models
from django.contrib.auth.models import User # Importa o modelo de usuário do Django

class Conta(models.Model):
    # O 'id' é criado automaticamente pelo Django
    numero_conta = models.CharField(max_length=20, unique=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contas')
    class Meta:
        db_table = 'tb_cad_conta'

class Transferencia(models.Model):
    # O 'id' é criado automaticamente
    remetente = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='transferencias_enviadas')
    destinatario = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='transferencias_recebidas')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True) # Preenchido automaticamente na criação

    class Meta:
        db_table = 'tb_acao_transferencia'

class Acao(models.Model):
    # O 'id' é criado automaticamente
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    preco_atual = models.DecimalField(max_digits=10, decimal_places=2)
    # Pode adicionar data da última atualização do preço, por exemplo
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_acao'

class CompraVendaAcao(models.Model):
    # O 'id' é criado automaticamente
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='compras_vendas_acoes') # Liga ao User do Django
    acao = models.ForeignKey(Acao, on_delete=models.CASCADE, related_name='operacoes_de_acao')
    quantidade = models.IntegerField()
    TIPO_CHOICES = [
        ('COMPRA', 'Compra'),
        ('VENDA', 'Venda'),
    ]
    tipo = models.CharField(max_length=6, choices=TIPO_CHOICES)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_acao_compra_venda_acao'

class Favorita(models.Model):
    # O 'id' é criado automaticamente
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='acoes_favoritas') # Liga ao User do Django
    acao = models.ForeignKey(Acao, on_delete=models.CASCADE, related_name='favoritada_por')

    class Meta:
       db_table = 'tb_cad_favorita'

    class Meta:
        unique_together = ('usuario', 'acao') # Garante que um usuário não favorite a mesma ação duas vezes