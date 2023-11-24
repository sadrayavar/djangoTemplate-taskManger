# Generated by Django 3.2.20 on 2023-11-24 10:24

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('priority', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('state', models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=11)),
                ('deadline_date', models.DateField(default=datetime.date.today)),
                ('deadline_time', models.TimeField(default=datetime.time(0, 0))),
            ],
        ),
    ]
