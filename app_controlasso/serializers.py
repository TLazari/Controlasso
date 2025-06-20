from rest_framework import serializers
from .models import Conta, Transferencia, Acao, CompraVendaAcao, Favorita
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = '__all__'


class TransferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transferencia
        fields = '__all__'


class AcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acao
        fields = '__all__'


class CompraVendaAcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompraVendaAcao
        fields = '__all__'


class FavoritaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorita
        fields = '__all__'
