# -*- coding: utf-8 -*-
import xadmin

from .models import Order


class OrderAdmin(object):
    list_display = ['id', 'user', 'goods', 'number', 'create_time', 'state', 'real_price','insurance_amount',
                    'sale_percentage', 'rebate_amount','compulsory_insurance_amount','compulsory_insurance_rebate_percentage',
                    'compulsory_rebate_amount', 'vehicle_and_vessel_tax', 'actual_slaes_section',
                    'incoming_slaes_section', 'is_received','receipt_time', 'actual_rebate', 'compulsory_actual_rebate',
                    'outstanding_corporation', 'profit', 'advances', 'cash_in_hand']
    search_fields = ['id', 'user', 'goods', 'number', 'state', 'insurance_amount', 'sale_percentage',  'actual_rebate']
    list_filter = ['id', 'user__username', 'goods__name', 'number', 'create_time', 'state', 'insurance_amount', 'sale_percentage', 'receipt_time', 'actual_rebate']



xadmin.site.register(Order, OrderAdmin)