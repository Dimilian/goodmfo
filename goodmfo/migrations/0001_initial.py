# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 22:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('patronymic', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(max_length=255)),
                ('homephone', models.CharField(max_length=255)),
                ('birth', models.CharField(max_length=255)),
                ('address_reg_index', models.CharField(max_length=255)),
                ('address_reg_region', models.CharField(max_length=255)),
                ('address_reg_district', models.CharField(blank=True, max_length=255, null=True)),
                ('address_reg_city', models.CharField(max_length=255)),
                ('address_reg_street', models.CharField(max_length=255)),
                ('address_reg_house', models.CharField(max_length=255)),
                ('address_reg_building', models.CharField(blank=True, max_length=255, null=True)),
                ('address_reg_apartment', models.CharField(blank=True, max_length=255, null=True)),
                ('address_fact_index', models.CharField(max_length=255)),
                ('address_fact_region', models.CharField(max_length=255)),
                ('address_fact_district', models.CharField(blank=True, max_length=255, null=True)),
                ('address_fact_city', models.CharField(max_length=255)),
                ('address_fact_street', models.CharField(max_length=255)),
                ('address_fact_house', models.CharField(max_length=255)),
                ('address_fact_building', models.CharField(blank=True, max_length=255, null=True)),
                ('address_fact_apartment', models.CharField(blank=True, max_length=255, null=True)),
                ('passport_serie', models.CharField(max_length=255)),
                ('passport_number', models.CharField(max_length=255)),
                ('kod', models.CharField(max_length=255)),
                ('passport_date', models.CharField(max_length=255)),
                ('passport_father', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('birthplace', models.CharField(max_length=255)),
                ('dohod', models.CharField(max_length=255)),
                ('izhd', models.CharField(max_length=255)),
                ('inn', models.CharField(blank=True, max_length=255, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
