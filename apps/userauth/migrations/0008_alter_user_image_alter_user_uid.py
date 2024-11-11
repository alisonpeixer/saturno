# Generated by Django 5.1.2 on 2024-11-10 17:46

import apps.userauth.models
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userauth", "0007_user_uid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(
                blank=True,
                default="/user_default/user_default.png",
                null=True,
                upload_to=apps.userauth.models.user_directory_path,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="uid",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet="abc1234567", length=10, max_length=20, prefix="uid"
            ),
        ),
    ]