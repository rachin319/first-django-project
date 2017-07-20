# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Goods(models.Model):
    id = models.CharField(max_length=8, primary_key=True, verbose_name=u'商品ID')
    name = models.CharField(max_length=100, verbose_name=u'商品名')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'单价')

    class Meta:
        verbose_name = u'商品信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name