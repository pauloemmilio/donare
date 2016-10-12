# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('categoria', models.CharField(max_length=100)),
                ('cnpj', models.IntegerField()),
                ('telefone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('agencia', models.IntegerField()),
                ('conta', models.IntegerField()),
                ('nomeTitular', models.CharField(max_length=200)),
                ('fotos', models.ImageField(blank=True, null=True, upload_to='static/img/ong')),
                ('videoUrl', models.URLField()),
                ('descricao', models.CharField(max_length=500)),
            ],
        ),
    ]