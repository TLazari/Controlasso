from django.contrib import admin
from django.urls import path
from users.views import register  # importa a view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),  # rota para a página de registro
]