from django.urls import path

from . import views

app_name = "core"

# URLS
urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('transferencia/', views.transferencia_view, name='transferencia'),
    path('transferencias/historico/', views.transferencias_historico_view, name='transferencias_historico'),
    path('acoes/', views.acoes_list_view, name='acoes_list'),
    path('acoes/favoritas/', views.acoes_favoritas_view, name='acoes_favoritas'),
    path('acoes/compradas/', views.acoes_compradas_view, name='acoes_compradas'),
    path('acoes/<str:codigo>/', views.acao_detail_view, name='acao_detail'),
    path('perfil/', views.perfil_view, name='perfil'),
]
