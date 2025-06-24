from django import template

register = template.Library()

"""
Filtros personalizados para uso em templates do Django.

Este módulo define filtros utilitários registrados no sistema de templates do Django,
permitindo operações comuns diretamente nos arquivos HTML dos templates.

Filtros definidos:
    - multiply: Multiplica dois valores numéricos.
    - brl: Formata um número no padrão monetário brasileiro (Real - R$).
    - get_item: Recupera um valor de um dicionário usando uma chave dinâmica.
"""

@register.filter
def multiply(value, arg):
    """
    Multiplica dois valores numéricos.

    Esse filtro tenta converter os argumentos para `float` e retorna
    o resultado da multiplicação.

    :param value: Primeiro valor (multiplicando)
    :param arg: Segundo valor (multiplicador)
    :return: Resultado da multiplicação ou string vazia em caso de erro
    :rtype: float or str
    """
    try:
        return float(value) * float(arg)
    except (TypeError, ValueError):
        return ""


@register.filter
def brl(value):
    """
    Formata um número no estilo monetário brasileiro (Real - R$).

    Exemplo: 1234.5 → 'R$ 1.234,50'

    :param value: Valor numérico a ser formatado
    :return: String com valor formatado em Real
    :rtype: str
    """
    try:
        number = float(value)
    except (TypeError, ValueError):
        return value
    formatted = "R$ {:,.2f}".format(number)
    return formatted.replace(",", "X").replace(".", ",").replace("X", ".")


@register.filter
def get_item(dictionary, key):
    """
    Recupera um valor de um dicionário usando uma chave dinâmica.

    Útil para acessar valores em dicionários em templates Django.

    :param dictionary: Dicionário do qual extrair o valor
    :param key: Chave a ser usada na busca
    :return: Valor correspondente à chave ou None
    :rtype: any
    """
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    return None
