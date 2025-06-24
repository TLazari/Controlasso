from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Account
import random


def generate_account_number():
    """
    Gera um número de conta único de 5 dígitos.
    
    Returns:
        str: Número de conta único
    """
    while True:
        number = str(random.randint(10000, 99999))
        if not Account.objects.filter(account_number=number).exists():
            return number


def generate_initial_balance():
    """
    Gera um saldo inicial aleatório entre 1000 e 10000.
    
    Returns:
        float: Saldo inicial
    """
    return round(random.uniform(1000, 10000), 2)


@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    """
    Cria uma conta automaticamente quando um novo usuário é registrado.
    
    Args:
        sender: Modelo que envia o sinal
        instance: Instância do usuário
        created: Se o usuário foi criado agora
        **kwargs: Argumentos adicionais
    """
    if created:
        Account.objects.create(
            user=instance,
            account_number=generate_account_number(),
            balance=generate_initial_balance(),
        )
        user_group, _ = Group.objects.get_or_create(name="Usuario")
        instance.groups.add(user_group)