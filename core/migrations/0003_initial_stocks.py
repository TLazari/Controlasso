from django.db import migrations


def create_initial_stocks(apps, schema_editor):
    Stock = apps.get_model('core', 'Stock')
    if Stock.objects.exists():
        return
    Stock.objects.create(name='Petrobras', code='PETR4', current_price=30.00)
    Stock.objects.create(name='Vale', code='VALE3', current_price=60.00)
    Stock.objects.create(name='Itaú Unibanco', code='ITUB4', current_price=25.00)

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0002_account_theme'),
    ]

    operations = [
        migrations.RunPython(create_initial_stocks),
    ]
