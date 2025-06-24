
import os

from django.core.wsgi import get_wsgi_application

"""
Configuração WSGI para o projeto projeto_controlasso.

Este arquivo expõe o callable WSGI como uma variável de módulo chamada ``application``.

Para mais informações sobre este arquivo, veja:
https://docs.djangoproject.com/pt-br/5.2/howto/deployment/wsgi/
"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_controlasso.settings')

application = get_wsgi_application()
