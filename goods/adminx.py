# -*- coding: utf-8 -*-
import xadmin

from .models import Goods


class GoodsAdmin(object):
    list_display = ['id', 'name', 'price']
    search_fields = ['id', 'name', 'price']
    list_filter = ['id', 'name', 'price']

xadmin.site.register(Goods, GoodsAdmin)