# Generated by Django 5.1.2 on 2024-11-05 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="produto",
            name="updated_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]