# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    activation = models.BooleanField(default=False, verbose_name=u'激活')
    key_id = models.CharField(max_length=10, verbose_name=u"推荐码", default=None)
    referee_key = models.CharField(max_length=10, verbose_name=u"推荐人Key", blank=True, null=True, default=None)
    referee_number = models.IntegerField(verbose_name=u"推荐人个数", default=0)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class Referee(models.Model):
    user = models.ForeignKey(UserProfile, related_name="user", verbose_name=u"被推荐人")
    referee = models.ForeignKey(UserProfile, related_name="referee", verbose_name=u"推荐人")
    is_active = models.BooleanField(verbose_name=u"有效", default=False)

    class Meta:
        verbose_name = u"推荐信息"
        verbose_name_plural = verbose_name


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=32, verbose_name=u'验证编码')
    email = models.EmailField(verbose_name=u'邮箱')
    send_type = models.CharField(choices=(('register', u'注册'), ('forget', u'找回密码')), max_length=10)

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.code