from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()
router.register(r'usuarios', UserViewSet)
router.register(r'contas', ContaViewSet)
router.register(r'transferencias', TransferenciaViewSet)
router.register(r'acoes', AcaoViewSet)
router.register(r'comprasvendas', CompraVendaAcaoViewSet)
router.register(r'favoritas', FavoritaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
