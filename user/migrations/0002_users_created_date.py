# Generated by Django 3.0.7 on 2020-07-09 16:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 16, 0, 12, 196336)),
        ),
    ]
