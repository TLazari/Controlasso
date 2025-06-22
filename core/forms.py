from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
    PasswordChangeForm,
)

from .models import Transfer, Trade, Stock, Account


class TransferForm(forms.ModelForm):
    account = forms.CharField(
        label="Conta",
        max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    recipient = forms.CharField(
        label="Usuário",
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "readonly": "readonly"}
        ),
    )

    class Meta:
        model = Transfer
        fields = ["amount"]
        widgets = {
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
        }


    def __init__(self, *args, current_user=None, **kwargs):
        self.current_user = current_user
        super().__init__(*args, **kwargs)
        self.fields["recipient"].initial = ""

    def clean_account(self):
        account_number = self.cleaned_data.get("account")
        try:
            account = Account.objects.get(account_number=account_number)
        except Account.DoesNotExist:
            raise forms.ValidationError("Conta n\u00e3o encontrada")
        if self.current_user and account.user == self.current_user:
            raise forms.ValidationError("N\u00e3o \u00e9 poss\u00edvel transferir para si mesmo")
        self.recipient_user = account.user
        return account_number

    def clean_amount(self):
        amount = self.cleaned_data.get("amount")
        if self.current_user and amount is not None:
            if self.current_user.account.balance < amount:
                raise forms.ValidationError("Saldo insuficiente")
        return amount

    def save(self, commit=True):
        transfer = super().save(commit=False)
        transfer.recipient = getattr(self, "recipient_user", None)
        if commit:
            transfer.save()
        return transfer


class TradeForm(forms.Form):
    stock = forms.ModelChoiceField(
        queryset=Stock.objects.all(), widget=forms.Select(attrs={"class": "form-select"})
    )
    quantity = forms.IntegerField(
        label="Quantidade",
        min_value=1,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    trade_type = forms.ChoiceField(
        label="Tipo",
        choices=[("buy", "Compra"), ("sell", "Venda")],
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    price = forms.DecimalField(
        label="Preço",
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    def __init__(self, *args, user=None, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if not self.user:
            return cleaned_data
        trade_type = cleaned_data.get("trade_type")
        quantity = cleaned_data.get("quantity")
        price = cleaned_data.get("price")
        stock = cleaned_data.get("stock")
        if not all([trade_type, quantity, price, stock]):
            return cleaned_data
        total = quantity * price
        if trade_type == Trade.BUY:
            if self.user.account.balance < total:
                raise forms.ValidationError("Saldo insuficiente")
        else:
            from django.db.models import Sum

            bought = (
                Trade.objects.filter(
                    user=self.user, stock=stock, trade_type=Trade.BUY
                ).aggregate(total=Sum("quantity"))
                ["total"]
                or 0
            )
            sold = (
                Trade.objects.filter(
                    user=self.user, stock=stock, trade_type=Trade.SELL
                ).aggregate(total=Sum("quantity"))
                ["total"]
                or 0
            )
            if quantity > bought - sold:
                raise forms.ValidationError(
                    "Quantidade não disponível para venda"
                )
        return cleaned_data


class StockTradeForm(forms.Form):
    trade_type = forms.ChoiceField(
        label="Tipo",
        choices=[("buy", "Compra"), ("sell", "Venda")],
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    quantity = forms.IntegerField(
        label="Quantidade",
        min_value=1,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    price = forms.DecimalField(
        label="Preço",
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    def __init__(self, *args, user=None, stock=None, **kwargs):
        self.user = user
        self.stock = stock
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if not self.user or not self.stock:
            return cleaned_data
        trade_type = cleaned_data.get("trade_type")
        quantity = cleaned_data.get("quantity")
        price = cleaned_data.get("price")
        if not all([trade_type, quantity, price]):
            return cleaned_data
        total = quantity * price
        if trade_type == "buy":
            if self.user.account.balance < total:
                raise forms.ValidationError("Saldo insuficiente")
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
            if quantity > bought - sold:
                raise forms.ValidationError(
                    "Quantidade não disponível para venda"
                )
        return cleaned_data


class BootstrapUserCreationForm(UserCreationForm):
    """UserCreationForm with Bootstrap CSS classes"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(self.error_messages["password_mismatch"], code="password_mismatch")
        return password2


class BootstrapAuthenticationForm(AuthenticationForm):
    """AuthenticationForm with Bootstrap CSS classes"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


class BootstrapPasswordResetForm(PasswordResetForm):
    """PasswordResetForm with Bootstrap CSS classes"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


class BootstrapSetPasswordForm(SetPasswordForm):
    """SetPasswordForm with Bootstrap CSS classes"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


class BootstrapPasswordChangeForm(PasswordChangeForm):
    """PasswordChangeForm with Bootstrap CSS classes"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


class AdminSetUserPasswordForm(forms.Form):
    username = forms.CharField(label="Usuário")
    new_password = forms.CharField(label="Nova senha", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
        self.user_obj = None

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            self.user_obj = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Usuário não encontrado")
        return username

    def save(self):
        from django.contrib.auth.password_validation import validate_password
        password = self.cleaned_data["new_password"]
        validate_password(password, self.user_obj)
        self.user_obj.set_password(password)
        self.user_obj.save()
        return self.user_obj


class DirectPasswordResetForm(forms.Form):
    """Reset a user's password directly by email."""

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    new_password1 = forms.CharField(
        label="Nova senha",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    new_password2 = forms.CharField(
        label="Confirmação",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("new_password1")
        p2 = cleaned_data.get("new_password2")
        if p1 and p2 and p1 != p2:
            self.add_error("new_password2", "A senha e a confirmação não correspondem.")
        return cleaned_data


class AdminUserUpdateForm(forms.Form):
    """Formulário para alterar senha e saldo de um usuário."""

    user_id = forms.IntegerField(widget=forms.HiddenInput)
    new_password1 = forms.CharField(
        label="Nova senha",
        required=False,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    balance = forms.DecimalField(
        label="Saldo",
        max_digits=12,
        decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def save(self):
        from django.contrib.auth.models import User

        user = User.objects.get(id=self.cleaned_data["user_id"])
        if self.cleaned_data.get("new_password1"):
            user.set_password(self.cleaned_data["new_password1"])
            user.save()
        account = user.account
        account.balance = self.cleaned_data["balance"]
        account.save()
        return user