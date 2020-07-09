# Generated by Django 3.0.7 on 2020-07-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=16)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
