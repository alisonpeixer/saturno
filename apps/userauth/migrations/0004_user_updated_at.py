# Generated by Django 5.1.2 on 2024-11-05 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userauth", "0003_alter_user_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="updated_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]