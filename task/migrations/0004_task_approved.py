# Generated by Django 5.0 on 2023-12-30 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0003_alter_task_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="approved",
            field=models.BooleanField(default=False),
        ),
    ]
