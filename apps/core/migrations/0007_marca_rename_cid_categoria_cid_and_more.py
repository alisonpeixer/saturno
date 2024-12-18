# Generated by Django 5.1.2 on 2024-11-05 17:35

import apps.core.models
import django.db.models.deletion
import shortuuid.django_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_alter_tags_options"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Marca",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "mid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="1234567890",
                        length=4,
                        max_length=4,
                        prefix="mid",
                        unique=True,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("descricao", models.TextField(blank=True, default="", null=True)),
                (
                    "imagem",
                    models.ImageField(upload_to=apps.core.models.marca_directory_path),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "Marcas",
            },
        ),
        migrations.RenameField(
            model_name="categoria",
            old_name="cId",
            new_name="cid",
        ),
        migrations.RenameField(
            model_name="produto",
            old_name="pId",
            new_name="pid",
        ),
        migrations.RenameField(
            model_name="tags",
            old_name="tId",
            new_name="tid",
        ),
        migrations.CreateModel(
            name="ProdutosImagens",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "imagens",
                    models.ImageField(upload_to=apps.core.models.produt_directory_path),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "produto",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.produto",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Imagens Produtos",
            },
        ),
        migrations.CreateModel(
            name="Vendedor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "vid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefgh1234567",
                        length=10,
                        max_length=20,
                        prefix="vid",
                        unique=True,
                    ),
                ),
                ("nome", models.CharField(max_length=70)),
                (
                    "imagem",
                    models.ImageField(
                        upload_to=apps.core.models.vendedor_directory_path
                    ),
                ),
                (
                    "marcas",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.marca",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Vendedores",
            },
        ),
    ]
