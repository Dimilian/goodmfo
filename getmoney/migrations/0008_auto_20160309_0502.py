# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-09 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getmoney', '0007_auto_20160228_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payvariant',
            name='payvar_image',
        ),
        migrations.AddField(
            model_name='payvariant',
            name='payvar_icon',
            field=models.CharField(default='note_add', max_length=100),
        ),
    ]
