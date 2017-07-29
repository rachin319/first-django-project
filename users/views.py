# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login, authenticate,logout
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from .form import LoginForm, RegisterForm, ForgetPwdForm, ModifyPwdForm
from .models import UserProfile, EmailVerifyRecord, Referee
from utils.email_send import send_register_email
from django.http import HttpResponseRedirect
from goods.models import Goods
from goods.views import generate_order_id

# Create your views here.
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                goods_items = Goods.objects.all()
                render(request, "goods.html", locals())
                return HttpResponseRedirect("/goods/")
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！"})
        else:
            return render(request, "login.html", {"login_form": login_form })


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, "logout.html")

    def post(self, request):
        logout(request)
        return render(request, "logout.html")


class ActiveUserView(View):
    def get(self, request, active_code):
        all_record = EmailVerifyRecord.objects.filter(code=active_code)
        if all_record:
            for record in all_record:
                email = record.email
                user = UserProfile.objects.filter(username=email)[0]
                if not user.activation:
                    user.activation = True
                    user.save()
                    if  Referee.objects.filter(user=user):
                        referee = Referee.objects.filter(user=user)[0]
                        referee.is_active = True
                        referee.referee.referee_number = referee.referee.referee_number + 1
                        referee.referee.save()
                        referee.save()

                else:
                    return render(request, "active_fail.html")
        else:
            return render(request, "active_fail.html")
        return HttpResponseRedirect("/login/")


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST.get("email", "")
            password = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = username
            user_profile.email = username
            try:
                if UserProfile.objects.get(email=username):
                    msg = u"该邮箱已注册！"
                    return render(request, "register.html", locals())
            except:
                pass
            referee = request.POST.get("referee", "")
            if referee == "":
                user_profile.referee_key = None
            else:
                if UserProfile.objects.filter(key_id=referee):
                   user_profile.referee_key = referee
                else:
                    msg = u"推荐码不存在"
                    return render(request, "register.html", locals())
            user_profile.key_id = generate_order_id(8)
            while UserProfile.objects.filter(key_id=user_profile.key_id):
                user_profile.key_id = generate_order_id(8)
            user_profile.password = make_password(password)
            user_profile.save()
            new_referee = Referee()
            if UserProfile.objects.filter(key_id=referee):
                new_referee.referee = UserProfile.objects.filter(key_id=referee)[0]
                if UserProfile.objects.filter(username=username):
                    new_referee.user = UserProfile.objects.filter(username=username)[0]
                    new_referee.save()
                else:
                    pass
            send_register_email(username, "register")
            return HttpResponseRedirect("/login/?message=success")
        else:
            return render(request, "register.html", {"register_form": register_form})


class RefereeView(View):
    def get(self, request):
        if request.user.is_authenticated():
            results = []
            for res in Referee.objects.filter(referee=request.user):
                if res.is_active:
                    results.append(res)
            return render(request, "referee.html", locals())
        else:
            return render(request, "login.html")

    def post(self, request):
        results = []
        for res in Referee.objects.filter(referee=request.user):
            if res.is_active:
                results.append(res)
        return render(request, "referee.html", locals())


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetPwdForm()
        return render(request, "forget_pwd.html", {"forget_form": forget_form})

    def post(self, request):
        forget_form = ForgetPwdForm(request.POST)
        if forget_form.is_valid():
            username = request.POST.get("email", "")
            send_register_email(username, "forget")
            return render(request, "forget_pwd.html", {"forget_form": forget_form, "success": "success"})
        else:
            return render(request, "forget_pwd.html", {"forget_form": forget_form})


class ResetView(View):
    def get(self, request, active_code):
        all_record = EmailVerifyRecord.objects.filter(code=active_code)
        if all_record:
            for record in all_record:
                email = record.email
                return render(request, "reset.html", {"username": email})
        else:
            return render(request, "active_fail.html")
        return HttpResponseRedirect("/login/")


class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("username", "")
            if pwd1 != pwd2:
                return render(request, "reset.html", {"username": email, "msg": "两次密码不一致！"})
            else:
                user = UserProfile.objects.filter(username=str(email))
                if user:
                    user[0].password = make_password(pwd1)
                    user[0].save()
                    return render(request, "login.html")
        else:
            email = request.POST.get("username", "")
            return render(request, "reset.html", {"username": email, "modify_form": modify_form})

        
class IndexView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                goods_items = Goods.objects.all()
                render(request, "goods.html", locals())
                return HttpResponseRedirect("/goods/")
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！"})
        else:
            return render(request, "login.html", {"login_form": login_form })


