# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-09 15:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170609_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='activation',
            new_name='is_activation',
        ),
    ]
