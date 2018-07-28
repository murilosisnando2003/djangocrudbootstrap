# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 22:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='River',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nome')),
                ('order', models.IntegerField(verbose_name='ordem')),
                ('length_km', models.FloatField(verbose_name='área (km²)')),
                ('basin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basins.Basin', verbose_name='bacia hidrográfica')),
            ],
        ),
    ]
