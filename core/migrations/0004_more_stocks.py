from django.db import migrations


def add_more_stocks(apps, schema_editor):
    Stock = apps.get_model('core', 'Stock')
    examples = [
        ('BBDC4', 'Banco Bradesco', 28.00),
        ('BBAS3', 'Banco do Brasil', 47.00),
        ('ABEV3', 'Ambev', 16.00),
    ]
    for code, name, price in examples:
        Stock.objects.get_or_create(code=code, defaults={'name': name, 'current_price': price})


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0003_initial_stocks'),
    ]

    operations = [
        migrations.RunPython(add_more_stocks),
    ]
