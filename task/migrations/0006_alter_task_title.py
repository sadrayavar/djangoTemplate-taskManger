# Generated by Django 5.0 on 2024-01-19 13:39

import taskManager.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0005_alter_task_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="title",
            field=models.CharField(
                max_length=15,
                unique=True,
                validators=[
                    taskManager.validator.validateNumber,
                    taskManager.validator.validateReserved,
                ],
            ),
        ),
    ]