# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-13 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('senha', models.CharField(max_length=50)),
                ('email', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'usuários',
                'verbose_name': 'usuário',
            },
        ),
    ]
