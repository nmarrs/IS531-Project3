# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_management', '0005_auto_20171120_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='date_acquired',
            field=models.DateField(blank=True, default='2017-11-19', null=True, verbose_name='date acquired'),
        ),
    ]