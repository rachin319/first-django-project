# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import UserProfile
from goods.models import Goods
from decimal import Decimal


# Create your models here.
class Order(models.Model):
    id = models.CharField(max_length=20, primary_key=True, verbose_name=u'订单ID')
    user = models.ForeignKey(UserProfile, related_name='user_set', verbose_name=u"用户ID")
    goods = models.ForeignKey(Goods, related_name='goods_set', verbose_name=u"商品ID")
    number = models.IntegerField(verbose_name=u"数量", default=1)
    create_time = models.DateField(verbose_name=u"创建时间", auto_now_add=True)
    real_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'成交价格', default=0)
    motorcycle_type = models.CharField(max_length=20, blank=True, verbose_name=u'车型')
    License_plate = models.CharField(max_length=20, blank=True, verbose_name=u'车牌')
    state = models.CharField(choices=(('completed', u'已完成'), ('pending', u'待处理'), ('closed', u'已关闭')), max_length=10, verbose_name=u'订单状态', default=u'待处理')
    insurance_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'商业险金额', default=0)
    sale_percentage = models.DecimalField(max_digits=6, decimal_places=5, verbose_name=u'商业险返点比例', default=0)
    compulsory_insurance_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'交强险金额', default=0)
    compulsory_insurance_rebate_percentage = models.DecimalField(max_digits=6, decimal_places=5, verbose_name=u'交强险返点比例', default=0)
    vehicle_and_vessel_tax = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'车船税', default=0)
    receipt_time = models.DateField(verbose_name=u'收款时间', blank=True, null=True)
    actual_rebate = models.DecimalField(max_digits=6, decimal_places=5, verbose_name=u'商业险实际返点', default=0)
    compulsory_actual_rebate = models.DecimalField(max_digits=6, decimal_places=5, verbose_name=u'交强险实际返点', default=0)
    is_received = models.BooleanField(verbose_name=u"已收", default=False)

    def rebate_amount(self):
        return Decimal.to_integral(self.insurance_amount*self.sale_percentage)
    rebate_amount.is_column = True
    rebate_amount.allow_tags = True
    rebate_amount.short_description = u'商业险返点金额'

    def compulsory_rebate_amount(self):
        return Decimal.to_integral(self.compulsory_insurance_amount*self.compulsory_insurance_rebate_percentage)
    compulsory_rebate_amount.is_column = True
    compulsory_rebate_amount.allow_tags = True
    compulsory_rebate_amount.short_description = u'交强险返点金额'

    def incoming_slaes_section(self):
        return Decimal.to_integral(self.real_price-self.actual_slaes_section())
    incoming_slaes_section.is_column = True
    incoming_slaes_section.allow_tags = True
    incoming_slaes_section.short_description = u'待收业务员款'

    def actual_slaes_section(self):
        return int(self.rebate_amount()+self.compulsory_rebate_amount())
    actual_slaes_section.is_column = True
    actual_slaes_section.allow_tags = True
    actual_slaes_section.short_description = u'给业务员总返点'

    def outstanding_corporation(self):
        return Decimal.to_integral((self.insurance_amount+self.compulsory_insurance_amount)/Decimal.from_float(1.06)*Decimal.from_float(0.38*(1-0.085)))
    outstanding_corporation.is_column = True
    outstanding_corporation.allow_tags = True
    outstanding_corporation.short_description = u'待收总公司款'

    def profit(self):
        return int(self.outstanding_corporation()+self.incoming_slaes_section()-self.real_price)
    profit.is_column = True
    profit.allow_tags = True
    profit.short_description = u'利润'

    def advances(self):
        return int((self.incoming_slaes_section() if not self.is_received else 0)+self.actual_slaes_section())
    advances.is_column = True
    advances.allow_tags = True
    advances.short_description = u'垫款'

    def cash_in_hand(self):
        return self.incoming_slaes_section()
    cash_in_hand.is_column = True
    cash_in_hand.allow_tags = True
    cash_in_hand.short_description = u'手头现金'

    class Meta:
        verbose_name = u'订单信息'
        verbose_name_plural = verbose_name
