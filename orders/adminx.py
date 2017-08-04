# -*- coding: utf-8 -*-
import xadmin

from .models import Order


class OrderAdmin(object):
    list_display = ['id', 'user', 'goods', 'number', 'create_time', 'motorcycle_type', 'License_plate',
                    'state', 'insurance_amount', 'compulsory_insurance_amount',
                    'vehicle_and_vessel_tax','sale_percentage', 'rebate_amount', 'total_price',
                    'incoming_slaes_section', 'is_received', 'receipt_time', 'actual_rebate',
                    'compulsory_actual_rebate', 'outstanding_corporation', 'profit', 'advances',
                    'cash_in_hand',
                    ]
    search_fields = ['id', 'user', 'goods', 'number', 'state', 'insurance_amount', 'sale_percentage',  'actual_rebate']
    list_filter = ['id', 'user__username', 'goods__name', 'number', 'create_time', 'state', 'insurance_amount', 'sale_percentage', 'receipt_time', 'actual_rebate']



xadmin.site.register(Order, OrderAdmin)