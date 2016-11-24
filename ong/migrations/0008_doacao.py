# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-24 02:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0007_onglogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('dataDeNascimento', models.CharField(max_length=10)),
                ('cpf', models.IntegerField()),
                ('valor', models.IntegerField()),
                ('ong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ong.Ong')),
            ],
        ),
    ]