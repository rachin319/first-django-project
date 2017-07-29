# -*- coding: utf-8 -*-
import xadmin

from .models import Credit


class CreditAdmin(object):
    list_display = ['use_date', 'user', 'bank','amount','bill_date','return_date','return_amount']
    search_fields = ['user','bank']
    list_filter = ['use_date', 'user', 'bank','amount','bill_date','return_date']

xadmin.site.register(Credit, CreditAdmin)
