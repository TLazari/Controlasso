from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    account_number = models.CharField(max_length=5, unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    theme = models.CharField(max_length=5, default="light")

    def __str__(self):
        return f"{self.user.username} - {self.account_number}"


class Transfer(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_transfers")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_transfers")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def execute(self):
        if self.sender.account.balance < self.amount:
            raise ValueError("Saldo insuficiente")
        self.sender.account.balance -= self.amount
        self.sender.account.save()
        self.recipient.account.balance += self.amount
        self.recipient.account.save()
        self.save()

    def __str__(self):
        return f"{self.sender.username} -> {self.recipient.username} ({self.amount})"


class Stock(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Trade(models.Model):
    BUY = "buy"
    SELL = "sell"
    TYPE_CHOICES = [
        (BUY, "Compra"),
        (SELL, "Venda"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    trade_type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def execute(self):
        total = self.quantity * self.price
        account = self.user.account
        if self.trade_type == Trade.BUY:
            if account.balance < total:
                raise ValueError("Saldo insuficiente")
            account.balance -= total
        else:
            from django.db.models import Sum

            bought = (
                Trade.objects.filter(
                    user=self.user, stock=self.stock, trade_type=Trade.BUY
                ).aggregate(total=Sum("quantity"))["total"]
                or 0
            )
            sold = (
                Trade.objects.filter(
                    user=self.user, stock=self.stock, trade_type=Trade.SELL
                ).aggregate(total=Sum("quantity"))["total"]
                or 0
            )
            if self.quantity > bought - sold:
                raise ValueError("Quantidade não disponível para venda")
            account.balance += total
        account.save()
        self.save()

    def __str__(self):
        return f"{self.get_trade_type_display()} {self.quantity} {self.stock.code}"


class FavoriteStock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "stock")

    def __str__(self):
        return f"{self.user.username} - {self.stock.code}"