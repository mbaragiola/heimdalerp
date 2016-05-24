# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0006_compensate_for_0003_bytestring_bug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='name')),
                ('initiated_activities', models.DateField(blank=True, null=True, verbose_name='initiated activities')),
            ],
            options={
                'verbose_name': 'company',
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='ExtraEmailAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('description', models.CharField(blank=True, default='', max_length=50, verbose_name='description')),
            ],
            options={
                'verbose_name': 'extra email address',
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'extra email addresses',
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=30, verbose_name='number')),
                ('phonenumber_type', models.CharField(choices=[('H', 'home'), ('W', 'work')], default='W', max_length=1, verbose_name='phone number type')),
                ('technology_type', models.CharField(choices=[('L', 'landline phone'), ('M', 'mobile phone')], default='M', max_length=1, verbose_name='technology type')),
            ],
            options={
                'verbose_name': 'phone number',
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'phone numbers',
            },
        ),
        migrations.CreateModel(
            name='PhysicalAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('F', 'fiscal'), ('H', 'home')], default='F', max_length=1, verbose_name='address type')),
                ('street_name', models.CharField(max_length=150, verbose_name='street name')),
                ('street_number', models.CharField(max_length=10, verbose_name='street number')),
                ('floor_number', models.CharField(default='', max_length=4, verbose_name='floor number')),
                ('apartment_number', models.CharField(default='', max_length=6, verbose_name='apartment number')),
                ('postal_code', models.CharField(max_length=20, verbose_name='postal code')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='physical_addresses', related_query_name='physical_address', to='cities_light.City', verbose_name='city')),
            ],
            options={
                'verbose_name': 'physical address',
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'physical addresses',
            },
        ),
    ]
