from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core.forms import (
    BootstrapAuthenticationForm,
    BootstrapPasswordChangeForm,
    BootstrapPasswordResetForm,
    BootstrapSetPasswordForm,
)
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", views.register, name="register"),
    # Alias to avoid 404s if Django's default registration path is used
    path("accounts/register/", views.register),

    path(
        "password-reset/",
        views.password_reset_direct,
        name="password_reset",
    ),
    path(
        "password-reset/delete/<int:user_id>/",
        views.delete_user,
        name="delete_user",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="registration/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html",
            form_class=BootstrapSetPasswordForm,
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            template_name="registration/password_change_form.html",
            form_class=BootstrapPasswordChangeForm,
        ),
        name="password_change",
    ),
    path(
        "password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="registration/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=BootstrapAuthenticationForm,
        ),
        name="login",
    ),
    # Django's default login path is "accounts/login/", add it to avoid 404s
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=BootstrapAuthenticationForm,
        ),
    ),
    path("logout/", views.logout_confirm, name="logout"),
    path("transfer/", views.make_transfer, name="transfer"),
    path("account-info/", views.account_info, name="account_info"),
    path("trade/", views.stock_list, name="trade"),
    path("trade/<int:stock_id>/", views.operate_stock, name="operate_stock"),
    path("api/stock-info/<int:stock_id>/", views.stock_info, name="stock_info"),
    path("trades/history/", views.trade_history, name="trade_history"),
    path("favorite/<int:stock_id>/", views.toggle_favorite_stock, name="toggle_favorite_stock"),
    path(
        "favorite-list/<int:stock_id>/",
        views.toggle_favorite_stock_list,
        name="toggle_favorite_stock_list",
    ),
    path("toggle-theme/", views.toggle_theme, name="toggle_theme"),
    path("", views.dashboard, name="dashboard"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)