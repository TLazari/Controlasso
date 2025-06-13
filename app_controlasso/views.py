from rest_framework import viewsets
from .models import Conta, Transferencia, Acao, CompraVendaAcao, Favorita
from .serializers import ContaSerializer, TransferenciaSerializer, AcaoSerializer, CompraVendaAcaoSerializer, FavoritaSerializer

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