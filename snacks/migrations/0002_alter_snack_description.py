# Generated by Django 4.1 on 2022-08-18 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snack',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
