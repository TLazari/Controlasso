from django.shortcuts import render


# Create your views here.
def dashboard_view(request):
    ...
    return render(request, "core/pages/dashboard.html")

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