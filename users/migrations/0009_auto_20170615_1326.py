# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-15 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_userprofile_referee_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='referee_key',
            field=models.CharField(default=None, max_length=10, null=True, verbose_name='\u63a8\u8350\u4ebaKey'),
        ),
    ]
