# Generated by Django 5.1.2 on 2024-11-10 17:21

import apps.userauth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userauth", "0005_user_tipo_usuario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(
                blank=True,
                default="/media/user_None/user_default.png",
                null=True,
                upload_to=apps.userauth.models.user_directory_path,
            ),
        ),
    ]