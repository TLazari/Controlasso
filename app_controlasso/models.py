from django.db import models
from django.contrib.auth.models import User


class Conta(models.Model):
    # Conta bancária do usuário
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contas')
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Conta de {self.user.username} - Saldo: {self.saldo}'


class Transferencia(models.Model):
    # Transferência entre contas
    conta_origem = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='transferencias_enviadas')
    conta_destino = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='transferencias_recebidas')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.conta_origem} -> {self.conta_destino} : {self.valor}'


class Acao(models.Model):
    # Cadastro de ações disponíveis
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.codigo} - {self.nome}'


class CompraVendaAcao(models.Model):
    # Registro de compra e venda de ações
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='acoes')
    acao = models.ForeignKey(Acao, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    tipo = models.CharField(max_length=4, choices=(('COMP', 'Compra'), ('VEND', 'Venda')))
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tipo} {self.quantidade} de {self.acao.codigo} - {self.conta}'


class Favorita(models.Model):
    # Ações favoritas do usuário
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritas')
    acao = models.ForeignKey(Acao, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.acao.codigo}'
