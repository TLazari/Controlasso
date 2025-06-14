from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("", views.login_view, name="login"),
    path("login/create/", views.login_create, name="login_create"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("register/create/", views.register_create, name="register_create"),
]
