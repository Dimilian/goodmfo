# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-27 14:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goodmfo', '0002_auto_20160227_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='client',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
