# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-16 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20170616_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='real_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='\u6210\u4ea4\u4ef7\u683c'),
        ),
    ]
