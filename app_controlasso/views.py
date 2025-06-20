from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Conta, Transferencia, Acao, CompraVendaAcao, Favorita
from .serializers import (
    UserSerializer,
    ContaSerializer,
    TransferenciaSerializer,
    AcaoSerializer,
    CompraVendaAcaoSerializer,
    FavoritaSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer


class TransferenciaViewSet(viewsets.ModelViewSet):
    queryset = Transferencia.objects.all()
    serializer_class = TransferenciaSerializer


class AcaoViewSet(viewsets.ModelViewSet):
    queryset = Acao.objects.all()
    serializer_class = AcaoSerializer


class CompraVendaAcaoViewSet(viewsets.ModelViewSet):
    queryset = CompraVendaAcao.objects.all()
    serializer_class = CompraVendaAcaoSerializer


class FavoritaViewSet(viewsets.ModelViewSet):
    queryset = Favorita.objects.all()
    serializer_class = FavoritaSerializer
