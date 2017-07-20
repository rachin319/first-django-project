# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-09 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_emailverifyrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='nick_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='activation',
            field=models.BooleanField(default=False),
        ),
    ]
