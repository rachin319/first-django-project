"""WebTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin

from users.views import LoginView, RegisterView, ActiveUserView, LogoutView, RefereeView, ForgetPwdView, ResetView, ModifyPwdView
from goods.views import GoodsView, SuccessView
from orders.views import OrdersView

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    url(r'^goods/', GoodsView.as_view(), name='goods'),
    url(r'^success/', SuccessView.as_view(), name='success'),
    url(r'^home/', OrdersView.as_view(), name='home'),
    url(r'^referee/', RefereeView.as_view(), name='referee'),
    url(r'^forget/', ForgetPwdView.as_view(), name='forget'),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url(r'^reset/$', ModifyPwdView.as_view(), name='reset'),
]
