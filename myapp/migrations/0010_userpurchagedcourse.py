# Generated by Django 3.0.7 on 2020-07-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_videos'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPurchagedCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('uid', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'user_purchaged_course',
            },
        ),
    ]
