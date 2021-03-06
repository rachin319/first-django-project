# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from .models import Goods
from orders.models import Order
from random import Random
from django.http import HttpResponseRedirect
from utils.email_send import send_register_email


# Create your views here.
class GoodsView(View):
    order_id = 0

    def get(self, request):
        goods_items = Goods.objects.all()
        return render(request, "goods.html", locals())

    def post(self, request):
        if self.request.user.is_authenticated() and self.request.user.activation:
            order = Order()
            #order.id = generate_order_id(16)
            self.order_id += 1
            order.id = str(self.order_id)
            while Order.objects.filter(id=order.id):
                self.order_id += 1
                order.id = str(self.order_id)
                #order.id = generate_order_id(16)
            order.user = self.request.user
            for item in self.request.POST:
                for i in range(8):
                    if Goods.objects.filter(id='0'*i+str(item)):
                        order.goods = Goods.objects.get(id='0'*i+str(item))
                        if order.goods.sale_percentage is not None:
                            order.sale_percentage = order.goods.sale_percentage
                        break
            order.state = 'pending'
            order.save()
            goods_items = Goods.objects.all()
            return render(request, "success.html", locals())
        elif self.request.user.is_authenticated():
            send_register_email(self.request.user.username, "register")
            return render(request, "goods.html", locals())
        else:
            return HttpResponseRedirect("/login/")


class SuccessView(View):
    def get(self, request):
        if self.request.user.is_authenticated():
            return render(request, "success.html", locals())
        else:
            return HttpResponseRedirect("/login/")

    def post(self):
        pass


def generate_order_id(randomlength):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiGgKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str