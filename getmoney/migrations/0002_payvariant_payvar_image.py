# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getmoney', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payvariant',
            name='payvar_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]