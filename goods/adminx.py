# -*- coding: utf-8 -*-
import xadmin

from .models import Goods


class GoodsAdmin(object):
    list_display = ['id', 'name', 'sale_percentage']
    search_fields = ['id', 'name', 'sale_percentage']
    list_filter = ['id', 'name', 'sale_percentage']

xadmin.site.register(Goods, GoodsAdmin)