"""stock URL Configuration
"""
from django.conf.urls import url
import stock.views

urlpatterns = [
    url(r'^$', stock.views.home, name='stock_name_url'),
    url(r'^(?P<ticker>[A-Za-z]+)/$', stock.views.detail, name='stock_detail_url'),   
]
