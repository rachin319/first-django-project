from django.shortcuts import render
from django.views.generic.base import View
from .models import Order
from goods.models import Goods
from django.http import HttpResponseRedirect
from users.models import UserProfile


# Create your views here.
class OrdersView(View):
    def get(self, request):
        if self.request.user.is_authenticated():
            order_list = Order.objects.filter(user_id=self.request.user.id)
            results = []
            for order in order_list:
                good = Goods.objects.get(id=str(order.goods_id))
                results.append({'id': order.id, 'goods': good.name, 'real_price': order.real_price,
                                'sale_percentage': good.sale_percentage,'create_time': order.create_time,
                                'state': order.state, 'motorcycle_type': order.motorcycle_type,
                                'license_plate': order.License_plate, 'rebate_amount': order.actual_slaes_section})
            return render(request, "home.html", locals())
        else:
            return HttpResponseRedirect("/login/")

    def post(self):
        pass
