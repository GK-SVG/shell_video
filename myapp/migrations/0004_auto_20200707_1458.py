# Generated by Django 3.0.7 on 2020-07-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200707_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecategary',
            name='image',
            field=models.ImageField(default='course_categary/course.png', upload_to='course_categary'),
        ),
    ]