# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 17:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, choices=[('computer', 'Computer'), ('phone', 'Phone'), ('software', 'Software'), ('car', 'Car'), ('rocket', 'Rocket')], null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='asset',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset_management.AssetName'),
        ),
    ]
