# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-30 05:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Bus'),
        ),
    ]
