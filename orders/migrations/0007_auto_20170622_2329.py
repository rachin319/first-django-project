# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-22 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20170616_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='actual_rebate',
            field=models.DecimalField(decimal_places=5, default=1, max_digits=6, verbose_name='\u5b9e\u9645\u8fd4\u70b9'),
        ),
        migrations.AddField(
            model_name='order',
            name='insurance_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='\u5546\u4e1a\u9669\u91d1\u989d'),
        ),
        migrations.AddField(
            model_name='order',
            name='receipt_time',
            field=models.DateField(blank=True, null=True, verbose_name='\u6536\u6b3e\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='order',
            name='sale_percentage',
            field=models.DecimalField(decimal_places=5, default=1, max_digits=6, verbose_name='\u9500\u552e\u8fd4\u70b9\u6bd4\u4f8b'),
        ),
    ]