
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^calculator/', 'getmoney.views.calculator'),
    url(r'^1/', 'getmoney.views.calculator'),
    url(r'^calculate/', 'getmoney.views.calculate'),
    url(r'^payvar/', 'getmoney.views.payvar'),
    url(r'^loan_submit/', 'getmoney.views.loan_submit'),
]
