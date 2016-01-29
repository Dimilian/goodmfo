
from django.conf.urls import include, url
from django.contrib import admin

import cabinet.views.polls

urlpatterns = [
    url(r'^/', 'getmoney.views.calculator'),
    url(r'^1/', 'getmoney.views.calculator'),
]
