from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import FormView
from django.urls import reverse_lazy
from django import forms
from django.forms.forms import NON_FIELD_ERRORS
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

from .models import Account, Transfer, Trade, Stock, FavoriteStock
from .forms import (
    TransferForm,
    TradeForm,
    BootstrapUserCreationForm,
    AdminSetUserPasswordForm,
    DirectPasswordResetForm,
)


class AdminPasswordResetView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = "registration/admin_set_user_password.html"
    form_class = AdminSetUserPasswordForm
    success_url = reverse_lazy("password_change_done")

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def register(request):
    if request.method == "POST":
        form = BootstrapUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = BootstrapUserCreationForm()
    return render(request, "register.html", {"form": form})


@login_required
def logout_confirm(request):
    """Display confirmation page and log the user out on POST."""
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return render(request, "registration/logout_confirm.html")


@login_required
def dashboard(request):
    account = request.user.account
    transfers_in = request.user.received_transfers.all()
    transfers_out = request.user.sent_transfers.all()

    start = request.GET.get("start")
    end = request.GET.get("end")
    from django.utils import timezone
    from datetime import datetime, timedelta

    if start:
        try:
            start_dt = timezone.make_aware(datetime.fromisoformat(start))
        except ValueError:
            start_dt = None
    else:
        start_dt = timezone.now() - timedelta(days=1)
        start = start_dt.isoformat(timespec="minutes")

    if end:
        try:
            end_dt = timezone.make_aware(datetime.fromisoformat(end))
        except ValueError:
            end_dt = None
    else:
        end_dt = timezone.now()
        end = end_dt.isoformat(timespec="minutes")

    if start_dt:
        transfers_in = transfers_in.filter(created_at__gte=start_dt)
        transfers_out = transfers_out.filter(created_at__gte=start_dt)
    if end_dt:
        transfers_in = transfers_in.filter(created_at__lte=end_dt)
        transfers_out = transfers_out.filter(created_at__lte=end_dt)
    trades = (
        Trade.objects.filter(user=request.user)
        .order_by("-created_at")[:5]
    )
    favorites = FavoriteStock.objects.filter(user=request.user)
    from collections import defaultdict

    in_summary = defaultdict(float)
    for t in transfers_in:
        hour = t.created_at.replace(minute=0, second=0, microsecond=0)
        in_summary[hour] += float(t.amount)

    out_summary = defaultdict(float)
    for t in transfers_out:
        hour = t.created_at.replace(minute=0, second=0, microsecond=0)
        out_summary[hour] += float(t.amount)

    trade_qs = Trade.objects.filter(user=request.user)
    if start_dt:
        trade_qs = trade_qs.filter(created_at__gte=start_dt)
    if end_dt:
        trade_qs = trade_qs.filter(created_at__lte=end_dt)
    trade_summary = defaultdict(float)
    for tr in trade_qs:
        hour = tr.created_at.replace(minute=0, second=0, microsecond=0)
        value = float(tr.quantity * tr.price)
        if tr.trade_type == Trade.BUY:
            value = -value
        trade_summary[hour] += value

    transfer_summary = defaultdict(float)
    for dt, amt in in_summary.items():
        transfer_summary[dt] += amt
    for dt, amt in out_summary.items():
        transfer_summary[dt] -= amt

    transfers_data = [
        {"date": dt.isoformat(timespec="minutes"), "amount": amt}
        for dt, amt in sorted(transfer_summary.items())
    ]
    trades_data = [
        {"date": dt.isoformat(timespec="minutes"), "amount": amt}
        for dt, amt in sorted(trade_summary.items())
    ]
    return render(
        request,
        "dashboard.html",
        {
            "account": account,
            "transfers_in": transfers_in,
            "transfers_out": transfers_out,
            "trades": trades,
            "favorites": favorites,
            "transfers_data": transfers_data,
            "trades_data": trades_data,
            "start": start,
            "end": end,
        },
    )


@login_required
def make_transfer(request):
    alert_message = None
    if request.method == "POST":
        form = TransferForm(request.POST, current_user=request.user)
        if form.is_valid():
            transfer = form.save(commit=False)
            transfer.sender = request.user
            try:
                transfer.execute()
                return redirect("dashboard")
            except ValueError as e:
                if str(e) == "Saldo insuficiente":
                    alert_message = str(e)
                else:
                    form.add_error(None, str(e))
        else:
            if "Saldo insuficiente" in form.errors.get("amount", []):
                alert_message = "Saldo insuficiente"
                form.errors["amount"].clear()
    else:
        form = TransferForm(current_user=request.user)
    return render(request, "transfer.html", {"form": form, "alert_message": alert_message})


@login_required
def account_info(request):
    """Return the username associated with an account number."""
    acc = request.GET.get("account")
    try:
        account = Account.objects.get(account_number=acc)
    except Account.DoesNotExist:
        return JsonResponse({"error": "not-found"}, status=404)
    if account.user == request.user:
        return JsonResponse({"error": "self"}, status=400)
    return JsonResponse({"user": account.user.username})


@login_required
def stock_list(request):
    """Display the list of stocks with user's favorites highlighted."""
    stocks = list(Stock.objects.all())
    fav_ids = set(
        FavoriteStock.objects.filter(user=request.user).values_list("stock_id", flat=True)
    )
    favorites = [s for s in stocks if s.id in fav_ids]
    others = [s for s in stocks if s.id not in fav_ids]
    return render(
        request,
        "trade_list.html",
        {"favorites": favorites, "stocks": others, "favorite_ids": fav_ids},
    )



@login_required
def operate_stock(request, stock_id):
    """Detailed page for trading a specific stock."""
    stock = Stock.objects.get(id=stock_id)

    from django.core.cache import cache
    import yfinance as yf

    cache_key = f"stock_data_{stock.code}"
    stock_data = cache.get(cache_key)
    if not stock_data:
        try:
            ticker = yf.Ticker(f"{stock.code}.SA")
            info = ticker.info
            hist = ticker.history(period="1d", interval="5m")
            prices = hist["Close"].tolist()
            dates = [d.isoformat() for d in hist.index]
            stock_data = {
                "price": info.get("regularMarketPrice"),
                "change": info.get("regularMarketChange"),
                "change_percent": info.get("regularMarketChangePercent"),
                "volume": info.get("regularMarketVolume"),
                "last_update": info.get("regularMarketTime"),
                "history": list(zip(dates, prices)),
                "description": info.get("longBusinessSummary", ""),
                "yahoo_url": f"https://finance.yahoo.com/quote/{stock.code}.SA",
            }
        except Exception:
            stock_data = {
                "price": stock.current_price,
                "change": 0,
                "change_percent": 0,
                "volume": 0,
                "last_update": "",
                "history": [],
                "description": "",
                "yahoo_url": f"https://finance.yahoo.com/quote/{stock.code}.SA",
            }
        cache.set(cache_key, stock_data, 900)

    alert_message = None
    if request.method == "POST":
        form = TradeForm(request.POST, user=request.user)
        if form.is_valid():
            trade = Trade(
                user=request.user,
                stock=stock,
                quantity=form.cleaned_data["quantity"],
                trade_type=form.cleaned_data["trade_type"],
                price=form.cleaned_data["price"],
            )
            try:
                trade.execute()
                from django.contrib import messages

                total = trade.quantity * trade.price
                if trade.trade_type == Trade.SELL:
                    messages.info(
                        request,
                        f"Venda realizada: {trade.quantity} a\u00e7\u00f5es por R$ {total:.2f}",
                    )
                else:
                    messages.info(
                        request,
                        f"Compra realizada: {trade.quantity} a\u00e7\u00f5es por R$ {total:.2f}",
                    )
                return redirect("operate_stock", stock_id=stock.id)
            except ValueError as e:
                if str(e) == "Saldo insuficiente":
                    alert_message = str(e)
                else:
                    form.add_error(None, str(e))
        else:
            if "Saldo insuficiente" in form.non_field_errors():
                alert_message = "Saldo insuficiente"
                form.errors[NON_FIELD_ERRORS].clear()
    else:
        form = TradeForm(
            initial={"stock": stock, "price": stock_data["price"]},
            user=request.user,
        )
    form.fields["stock"].widget = forms.HiddenInput()

    history = [
        {
            "date": t.created_at,
            "type": t.get_trade_type_display(),
            "quantity": t.quantity,
            "price": t.price,
            "total": t.quantity * t.price,
        }
        for t in Trade.objects.filter(user=request.user, stock=stock).order_by("-created_at")
    ]

    from django.db.models import Sum
    bought = (
        Trade.objects.filter(user=request.user, stock=stock, trade_type=Trade.BUY).aggregate(total=Sum("quantity"))["total"]
        or 0
    )
    sold = (
        Trade.objects.filter(user=request.user, stock=stock, trade_type=Trade.SELL).aggregate(total=Sum("quantity"))["total"]
        or 0
    )
    owned_qty = bought - sold

    is_favorite = FavoriteStock.objects.filter(user=request.user, stock=stock).exists()

    return render(
        request,
        "operate_stock.html",
        {
            "stock": stock,
            "form": form,
            "data": stock_data,
            "balance": request.user.account.balance,
            "history": history,
            "is_favorite": is_favorite,
            "alert_message": alert_message,
            "owned_quantity": owned_qty,
        },
    )


@login_required
def stock_info(request, stock_id):
    """Return chart and price change data for a single stock."""
    stock = get_object_or_404(Stock, id=stock_id)

    from django.core.cache import cache
    import yfinance as yf

    cache_key = f"stock_chart_{stock.code}"
    data = cache.get(cache_key)
    if not data:
        try:
            ticker = yf.Ticker(f"{stock.code}.SA")
            info = ticker.info
            change = info.get("regularMarketChangePercent", 0)
            hist = ticker.history(period="1d", interval="60m")
            prices = hist["Close"].tolist()
            dates = [d.isoformat() for d in hist.index]
            chart = list(zip(dates, prices))[-4:]
            data = {"hist": chart, "change": change}
        except Exception:
            data = {"hist": [], "change": 0}
        cache.set(cache_key, data, 900)

    return JsonResponse(data)


@require_POST
@login_required
def toggle_favorite_stock(request, stock_id):
    """Add or remove a stock from the user's favorites."""
    stock = Stock.objects.get(id=stock_id)
    fav, created = FavoriteStock.objects.get_or_create(user=request.user, stock=stock)
    if not created:
        fav.delete()
    return redirect("operate_stock", stock_id=stock.id)


@require_POST
@login_required
def toggle_favorite_stock_list(request, stock_id):
    """Toggle favorite status from the stock list view."""
    stock = Stock.objects.get(id=stock_id)
    fav, created = FavoriteStock.objects.get_or_create(user=request.user, stock=stock)
    if not created:
        fav.delete()
    return redirect("trade")


@require_POST
@login_required
def add_favorite(request, stock_id):
    stock = Stock.objects.get(id=stock_id)
    FavoriteStock.objects.get_or_create(user=request.user, stock=stock)
    return redirect("operate_stock", stock_id=stock_id)


@login_required
def trade_history(request):
    """List all stock trades for the current user."""
    trades = Trade.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "trade_history.html", {"trades": trades})


@require_POST
@login_required
def toggle_theme(request):
    theme = request.POST.get("theme")
    if theme not in {"light", "dark"}:
        return JsonResponse({"error": "invalid"}, status=400)
    account = request.user.account
    account.theme = theme
    account.save()
    return JsonResponse({"theme": theme})


@login_required
def password_reset_direct(request):
    """Permite alterar senha e saldo de todos os usuários."""

    from django.contrib.auth.models import User
    from .forms import AdminUserUpdateForm

    if not request.user.is_staff:
        return redirect("login")

    users = User.objects.all().select_related("account").order_by("username")

    if request.method == "POST":
        forms = []
        valid = True
        for user in users:
            form = AdminUserUpdateForm(request.POST, prefix=str(user.id))
            forms.append((user, form))
            if form.is_valid():
                form.save()
            else:
                valid = False
        if valid:
            return redirect("password_reset")
    else:
        forms = [
            (
                user,
                AdminUserUpdateForm(
                    prefix=str(user.id),
                    initial={
                        "user_id": user.id,
                        "balance": user.account.balance,
                    },
                ),
            )
            for user in users
        ]

    return render(
        request,
        "registration/password_reset_direct.html",
        {"forms": forms},
    )


@login_required
def delete_user(request, user_id):
    if not request.user.is_staff:
        return redirect("login")
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.delete()
        return redirect("password_reset")
    return render(request, "registration/delete_user_confirm.html", {"user": user})