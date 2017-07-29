# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Goods(models.Model):
    id = models.CharField(max_length=8, primary_key=True, verbose_name=u'商品ID')
    name = models.CharField(max_length=100, verbose_name=u'商品名')
    sale_percentage = models.DecimalField(max_digits=6, decimal_places=5, verbose_name=u'返点比例', blank=True, null=True)
    #price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u'商业险返点比例', blank=True)

    class Meta:
        verbose_name = u'商品信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name