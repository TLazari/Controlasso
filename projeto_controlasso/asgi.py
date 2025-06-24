
import os

from django.core.asgi import get_asgi_application

"""
Configuração ASGI para o projeto projeto_controlasso.

Este arquivo expõe o callable ASGI como uma variável de módulo chamada ``application``.

O ASGI (Asynchronous Server Gateway Interface) é a especificação padrão para
aplicações Django assíncronas, sendo o sucessor do WSGI.

Para mais informações sobre este arquivo, veja:
https://docs.djangoproject.com/pt-br/5.2/howto/deployment/asgi/
"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_controlasso.settings')

application = get_asgi_application()
