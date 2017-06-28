# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 23:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nfc_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('bus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.Bus')),
            ],
        ),
    ]
