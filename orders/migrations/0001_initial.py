# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-09 02:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='\u8ba2\u5355ID')),
                ('number', models.IntegerField(verbose_name='\u6570\u91cf')),
                ('create_time', models.DateField(verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('state', models.CharField(choices=[('completed', '\u5df2\u5b8c\u6210'), ('pending', '\u5f85\u5904\u7406'), ('closed', '\u5df2\u5173\u95ed')], max_length=10)),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_set', to='goods.Goods', verbose_name='\u5546\u54c1ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_set', to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237ID')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355\u4fe1\u606f',
                'verbose_name_plural': '\u8ba2\u5355\u4fe1\u606f',
            },
        ),
    ]
