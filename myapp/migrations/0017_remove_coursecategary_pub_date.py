# Generated by Django 3.0.7 on 2020-09-21 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20200921_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursecategary',
            name='pub_date',
        ),
    ]
