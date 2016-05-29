"""crabtheme URL Configuration
"""
from django.conf.urls import url
import crabtheme.views

urlpatterns = [
    url(r'^$', crabtheme.views.home, name='home_name_url'),
]
