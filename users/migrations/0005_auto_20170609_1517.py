# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-09 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170609_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_activation',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='activation',
            field=models.BooleanField(default=False, verbose_name='\u6fc0\u6d3b'),
        ),
    ]