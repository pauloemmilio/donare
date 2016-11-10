# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-10 00:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ong', '0006_auto_20161108_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='OngLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ong', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ong.Ong')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]