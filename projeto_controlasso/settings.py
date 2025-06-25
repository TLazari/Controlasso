"""
Configuração do Django para o projeto projeto_controlasso.

Gerado com o comando 'django-admin startproject' usando Django 5.2.2.

Para mais informações sobre este arquivo, veja:
https://docs.djangoproject.com/pt-br/5.2/topics/settings/

Para a lista completa de configurações e seus valores, acesse:
https://docs.djangoproject.com/pt-br/5.2/ref/settings/
"""

from pathlib import Path

# Caminho base do projeto (raiz), usado para construir outros caminhos relativos no projeto.
BASE_DIR = Path(__file__).resolve().parent.parent

# ===========================
# ⚠️ Configurações de Segurança
# ===========================

# Chave secreta usada para criptografia e segurança do Django.
# IMPORTANTE: nunca expor essa chave em produção!
SECRET_KEY = 'django-insecure-!eqj0h2(-tmk8cr_(t$1tgv!xl^w=tsz5&2pl!cm8y)=u8(69t'

# Modo de depuração — deve estar em False em produção.
DEBUG = True

# Lista de hosts permitidos a acessar o sistema.
ALLOWED_HOSTS = ['*']


# ===========================
# 🧩 Aplicativos Instalados
# ===========================

INSTALLED_APPS = [
    # Aplicativos padrão do Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Aplicativos customizados do projeto
    'core',
]

# ===========================
# 🧱 Middleware
# ===========================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ===========================
# 🌐 Configuração de URLs e Templates
# ===========================

# Arquivo principal de roteamento do projeto
ROOT_URLCONF = 'projeto_controlasso.urls'

# Configurações dos templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Diretório onde os templates personalizados ficam
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Aplicação WSGI — ponto de entrada para servidores compatíveis
WSGI_APPLICATION = 'projeto_controlasso.wsgi.application'

# ===========================
# 💾 Banco de Dados
# ===========================

# Banco de dados padrão (SQLite para desenvolvimento)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ===========================
# 🔐 Validações de Senha
# ===========================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ===========================
# 🌍 Internacionalização
# ===========================

LANGUAGE_CODE = 'pt-BR'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# ===========================
# 🖼️ Arquivos Estáticos
# ===========================

# URL base para servir arquivos estáticos (CSS, JS, imagens)
STATIC_URL = 'static/'

# Diretório onde os arquivos estáticos serão coletados (ex: para deploy)
STATIC_ROOT = BASE_DIR / "staticfiles"

# Diretórios adicionais de arquivos estáticos durante o desenvolvimento
STATICFILES_DIRS = [BASE_DIR / "static"]

# ===========================
# 🔑 Configuração de campo padrão para chaves primárias
# ===========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ===========================
# 🔐 Autenticação
# ===========================

# URL para onde o usuário será redirecionado ao tentar acessar algo sem estar logado
LOGIN_URL = "/accounts/login/"

# URL para onde o usuário é redirecionado após login com sucesso
LOGIN_REDIRECT_URL = "/"

# URL para onde o usuário é redirecionado após logout (None = mostra tela de logout)
LOGOUT_REDIRECT_URL = None

# ===========================
# 📧 Backend de e-mail (ambiente de desenvolvimento)
# ===========================

# Backend de e-mail que imprime no console (útil para testes)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

TEST_RUNNER = 'django.test.runner.DiscoverRunner'  # default
