# Generated by Django 5.1.2 on 2024-12-29 18:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_itenspedidovenda_produto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='Carrinho',
        ),
        migrations.AlterModelOptions(
            name='carrinho',
            options={'verbose_name_plural': 'Carinhos'},
        ),
    ]
