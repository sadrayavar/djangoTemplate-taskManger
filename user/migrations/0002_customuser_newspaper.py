# Generated by Django 5.0 on 2024-01-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="newspaper",
            field=models.BooleanField(default=False),
        ),
    ]