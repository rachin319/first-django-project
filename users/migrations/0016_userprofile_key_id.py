# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-16 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20170616_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='key_id',
            field=models.CharField(default=None, max_length=10, verbose_name='\u63a8\u8350\u7801'),
        ),
    ]