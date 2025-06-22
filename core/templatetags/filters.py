from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (TypeError, ValueError):
        return ""

@register.filter
def brl(value):
    """Format a numeric value using Brazilian Real style."""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return value
    formatted = "R$ {:,.2f}".format(number)
    return formatted.replace(",", "X").replace(".", ",").replace("X", ".")


@register.filter
def get_item(dictionary, key):
    """Retrieve a value from a dict using a dynamic key."""
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    return None