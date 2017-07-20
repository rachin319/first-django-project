# -*- coding:utf-8 -*-
from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)
    capcha = CaptchaField(error_messages={"invalid": "验证码错误"})


class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    capcha = CaptchaField(error_messages={"invalid": "验证码错误"})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)