from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContaViewSet, TransferenciaViewSet, AcaoViewSet, CompraVendaAcaoViewSet, FavoritaViewSet

router = DefaultRouter()
router.register(r'contas', ContaViewSet)
router.register(r'transferencias', TransferenciaViewSet)
router.register(r'acoes', AcaoViewSet)
router.register(r'compras-vendas', CompraVendaAcaoViewSet)
router.register(r'favoritas', FavoritaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]