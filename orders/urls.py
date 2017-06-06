"""orders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from findorders import views as orders_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #显示orders订单号
    url(r'^home/$', orders_view.home),
    url(r'^finddelivery/$', orders_view.finddelivery,name='finddelivery'),
    url(r'^getresults/', orders_view.get_request),
    #导出订单
    url(r'^export/$', orders_view.xls_mould, name='xls_mould'),
]
