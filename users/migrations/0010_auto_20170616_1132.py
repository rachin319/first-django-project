# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-16 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20170615_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='referee_key',
            field=models.CharField(blank=True, default=None, max_length=10, verbose_name='\u63a8\u8350\u4ebaKey'),
        ),
    ]