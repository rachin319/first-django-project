# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-29 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20170729_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='sale_percentage',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True, verbose_name='\u5546\u4e1a\u9669\u8fd4\u70b9\u6bd4\u4f8b'),
        ),
    ]
