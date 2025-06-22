from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Account
import random


def generate_account_number():
    """Generate a unique 5-digit account number."""
    while True:
        number = str(random.randint(10000, 99999))
        if not Account.objects.filter(account_number=number).exists():
            return number


def generate_initial_balance():
    return round(random.uniform(1000, 10000), 2)


@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(
            user=instance,
            account_number=generate_account_number(),
            balance=generate_initial_balance(),
        )
        user_group, _ = Group.objects.get_or_create(name="Usuario")
        instance.groups.add(user_group)