# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-22 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20170622_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='rebate_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='\u8fd4\u70b9\u91d1\u989d'),
        ),
    ]