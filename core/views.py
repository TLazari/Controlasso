from django.contrib.auth.models import User
from django.shortcuts import render

from app_controlasso.models import (  #import dos models
    Acao,
    CompraVendaAcao,
    Conta,
    Favorita,
    Transferencia,
)


# Create your views here.
def dashboard_view(request):
    ... # No lugar dos tres pontinhos fica a comunicação do database vulgo models, com o front ent
    #tipo nos falamos data base para enviar a tabela como objeto 
    usuarios = User.objects.order_by('username')  # aqui eu pedi só os usuarios relacionados
    
    context = { #atribuo tudo que quero para ser enviado nessa variavel 
        'usuarios': usuarios,
    }
    
    return render(request, "core/pages/dashboard.html", context) # envio

def transferencia_view(request):
    ...
    return render(request, "core/pages/transferencia.html")

def transferencias_historico_view(request):
    ...
    return render(request, "core/pages/transferencias_historico.html")

def acoes_list_view(request):
    ...
    return render(request, "core/pages/acoes_list.html")

def acoes_favoritas_view(request):
    ...
    return render(request, "core/pages/acoes_favoritas.html")

def acoes_compradas_view(request):
    ...
    return render(request, "core/pages/acoes_compradas.html")

def acao_detail_view(request):
    ...
    return render(request, "core/pages/acao_detail.html")

def perfil_view(request):
    ...
    return render(request, "core/pages/perfil.html")

def home_view(request):
    ...
    return render(request, "core/pages/home.html")
