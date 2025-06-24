from django.apps import AppConfig

"""
Configuração do aplicativo 'core' do projeto.

Define a configuração padrão do aplicativo, incluindo o tipo
padrão para chaves primárias automáticas e o carregamento
de sinais ao iniciar o aplicativo.

Atributos:
    default_auto_field (str): Tipo padrão para campos auto incrementais (BigAutoField).
    name (str): Nome do aplicativo Django.

Métodos:
    ready(): Importa o módulo de sinais para registrar handlers de eventos.
"""

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    
    def ready(self):
        from . import signals  # noqa
