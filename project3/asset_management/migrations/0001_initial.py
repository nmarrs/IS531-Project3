# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 23:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.TextField(blank=True, choices=[('C', 'Computer'), ('P', 'Phone'), ('S', 'Software'), ('C', 'Car'), ('R', 'Rocket')], null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('maintenance_notes', models.TextField(blank=True, null=True)),
                ('date_implemented', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('role', models.TextField(blank=True, choices=[('A', 'Admin'), ('M', 'Manager'), ('E', 'Employee')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(blank=True, choices=[('SJ', 'San Jose, CA, USA'), ('LA', 'Los Angeles, CA, USA'), ('D', 'Denver, CO, USA'), ('M', 'Madrid, Spain'), ('P', 'Paris, France'), ('B', 'Beijing, China')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, choices=[('D', 'Dell'), ('A', 'Apple'), ('T', 'Tesla'), ('SX', 'SpaceX'), ('M', 'Microsoft')], null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, choices=[('MO', 'MyOrg'), ('EO', 'ExampleOrg')], null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='employee',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='asset_management.Employee'),
        ),
        migrations.AddField(
            model_name='asset',
            name='location',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='asset_management.Location'),
        ),
        migrations.AddField(
            model_name='asset',
            name='manufacturer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='asset_management.Manufacturer'),
        ),
        migrations.AddField(
            model_name='asset',
            name='organization',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='asset_management.Organization'),
        ),
    ]
