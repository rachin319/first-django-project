# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Referee


# Register your models here.
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = u'后台管理系统'
    site_footer = u"XX网"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type']


class RefereeAdmin(object):
    list_display = ['user', 'referee', 'is_active']
    search_fields = ['user', 'referee', 'is_active']
    list_filter = ['user', 'referee', 'is_active']

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Referee, RefereeAdmin)
