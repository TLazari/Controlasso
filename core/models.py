from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    """
    Modelo que representa uma conta bancária de um usuário.

    Atributos:
        user (OneToOneField): Referência ao usuário do sistema.
        account_number (CharField): Número único da conta (5 dígitos).
        balance (DecimalField): Saldo da conta.
        theme (CharField): Tema da interface (claro/escuro).

    Métodos:
        __str__: Retorna uma representação em string do objeto.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    account_number = models.CharField(max_length=5, unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    theme = models.CharField(max_length=5, default="light")

    def __str__(self):
        return f"{self.user.username} - {self.account_number}"


class Transfer(models.Model):
    """
    Modelo que representa uma transferência entre contas.

    Atributos:
        sender (ForeignKey): Usuário que envia o dinheiro.
        recipient (ForeignKey): Usuário que recebe o dinheiro.
        amount (DecimalField): Valor da transferência.
        created_at (DateTimeField): Data e hora da criação.

    Métodos:
        execute: Processa a transferência, atualizando os saldos.
        __str__: Retorna uma representação em string do objeto.
    """
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_transfers")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_transfers")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def execute(self):
        """
        Executa a transferência, verificando saldo e atualizando contas.
        
        Raises:
            ValueError: Se o saldo do remetente for insuficiente.
        """
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
    """
    Modelo que representa uma ação na bolsa de valores.

    Atributos:
        name (CharField): Nome da empresa.
        code (CharField): Código da ação na bolsa.
        current_price (DecimalField): Preço atual da ação.

    Métodos:
        __str__: Retorna uma representação em string do objeto.
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Trade(models.Model):
    """
    Modelo que representa uma operação de compra ou venda de ações.

    Atributos:
        BUY (str): Constante para tipo de operação de compra.
        SELL (str): Constante para tipo de operação de venda.
        TYPE_CHOICES (list): Lista de opções para o tipo de operação.
        user (ForeignKey): Usuário que realiza a operação.
        stock (ForeignKey): Ação negociada.
        quantity (PositiveIntegerField): Quantidade de ações.
        trade_type (CharField): Tipo de operação (compra ou venda).
        price (DecimalField): Preço da ação no momento da operação.
        created_at (DateTimeField): Data e hora da criação.

    Métodos:
        execute: Processa a operação, verificando saldo e atualizando contas.
        __str__: Retorna uma representação em string do objeto.
    """
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
        """
        Executa a operação de compra ou venda, verificando saldo ou quantidade.
        
        Raises:
            ValueError: Se o saldo for insuficiente para compra ou 
                        se a quantidade for insuficiente para venda.
        """
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
    """
    Modelo que representa uma ação favoritada por um usuário.

    Atributos:
        user (ForeignKey): Usuário que favoritou.
        stock (ForeignKey): Ação favoritada.

    Meta:
        unique_together: Garante que um usuário só pode favoritar uma ação uma vez.
        
    Métodos:
        __str__: Retorna uma representação em string do objeto.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "stock")

    def __str__(self):
        return f"{self.user.username} - {self.stock.code}"