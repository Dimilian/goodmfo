# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-09 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodmfo', '0006_auto_20160309_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='bank_bik',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='bank_ls',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]