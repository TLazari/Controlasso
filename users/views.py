from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, RegisterForm

# Create your views here.

def home_TEMPORARIA(request):
    return render(request,
        "users/pages/home_TEMPORARIA.html")


def register_view(request):
    """View para renderizar a página de register."""
    register_form_data = request.session.get("register_form_data", None)
    form = RegisterForm(register_form_data)

    return render(
        request,
        "users/pages/register.html",
        context={
            "form": form,
        },
    )


def register_create(request):
    """View para validar."""
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session["register_form_data"] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, "Usuário cadastrado com sucesso!")
        del request.session["register_form_data"]
        return redirect("users:login")

    return redirect("users:register")


def login_view(request):
    """View para renderizar a página de login."""
    if request.user.is_authenticated:
        # Redireciona para o dashboard se o usuário já estiver logado
        # Isso evita que o fluxo de login_create seja acionado novamente após um logout falho ou redirecionamento.
        return redirect(
            "users:home_TEMPORARIA"
        )  # Certifique-se que 'dashboard' é o nome da sua URL para o dashboard
    form = LoginForm()
    return render(
        request,
        "users/pages/login.html",
        context={
            "form": form,
            "form_action": reverse("users:login_create"),
        },
    )


def login_create(request):
    """View para validar o login."""
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticate_user = authenticate(
            username=form.cleaned_data.get("username", ""),
            password=form.cleaned_data.get("password", ""),
        )

        if authenticate_user is not None:
            login(request, authenticate_user)
        else:
            messages.error(request, "Credenciais invalidas")
            return redirect("users:login")
    else:
        messages.error(request, "Nome de usuario ou senha invalidos.")

    return redirect("users:home_TEMPORARIA")

@login_required(login_url="users:login", redirect_field_name="next")
def logout_view(request):
    logout(request)
    messages.info(request, "Você foi desconectado com sucesso.")
    return redirect(reverse("users:login"))
