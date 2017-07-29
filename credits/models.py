# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from decimal import Decimal
from datetime import *
# Create your models here.


class Credit(models.Model):
    use_date = models.DateField(verbose_name=u"刷卡日期")
    amount = models.DecimalField(verbose_name=u"刷卡金额", max_digits=10, decimal_places=2)
    user = models.CharField(verbose_name=u"刷卡人", max_length=20)
    bank = models.CharField(verbose_name=u"卡行", max_length=100)
    bill_date = models.DateField(verbose_name=u"账单日")
    return_date = models.DateField(verbose_name=u"还款日")
    def return_amount(self):
        amount = Decimal.from_float(0)
        date_end = str(self.bill_date.year)+'-'+str(self.bill_date.month).zfill(2)+'-'+str(self.bill_date.day)
        date_sta = str(self.bill_date.year)+'-'+str(self.bill_date.month-1).zfill(2)+'-'+str(self.bill_date.day)
        for item in Credit.objects.filter(user=self.user, bank=self.bank, use_date__range=[date_sta, date_end]):
             amount += item.amount
        return amount
    return_amount.is_column = True
    return_amount.allow_tags = True
    return_amount.short_description = u'本期还款金额'


