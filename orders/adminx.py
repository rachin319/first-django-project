# -*- coding: utf-8 -*-
import xadmin

from .models import Order


class OrderAdmin(object):
    list_display = ['id', 'user', 'goods', 'number', 'create_time', 'state', 'real_price','insurance_amount',
                    'sale_percentage', 'rebate_amount', 'incoming_slaes_section', 'is_received',
                    'receipt_time', 'actual_rebate', 'outstanding_corporation', 'profit', 'advances']
    search_fields = ['id', 'user', 'goods', 'number', 'state', 'insurance_amount', 'sale_percentage',  'actual_rebate']
    list_filter = ['id', 'user__username', 'goods__name', 'number', 'create_time', 'state', 'insurance_amount', 'sale_percentage', 'receipt_time', 'actual_rebate']



xadmin.site.register(Order, OrderAdmin)