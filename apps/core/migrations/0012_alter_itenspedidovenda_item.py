# Generated by Django 5.1.2 on 2024-11-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_alter_itenspedidovenda_item"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itenspedidovenda",
            name="item",
            field=models.CharField(default="0000", max_length=4),
        ),
    ]