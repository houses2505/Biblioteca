# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-10-07 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(max_length=10)),
                ('nombre_libro', models.CharField(max_length=200)),
                ('nombre_autor', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=20)),
            ],
        ),
    ]
