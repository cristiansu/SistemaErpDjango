# Generated by Django 4.0.3 on 2022-04-22 05:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_category_date_creation_category_date_updated_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='sexo',
            new_name='gender',
        ),
        migrations.RemoveField(
            model_name='client',
            name='birthday',
        ),
        migrations.AddField(
            model_name='client',
            name='date_birthday',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='client',
            name='dni',
            field=models.CharField(max_length=10, unique=True, verbose_name='Dni'),
        ),
    ]