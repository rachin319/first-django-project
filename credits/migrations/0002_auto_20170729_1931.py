# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-29 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='use_date',
            field=models.DateField(verbose_name='\u5237\u5361\u65e5\u671f'),
        ),
    ]
