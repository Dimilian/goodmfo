from django.db import models
from django.contrib.auth.models import User


class Loan(models.Model):
    client = models.ForeignKey(User)
    date_add = models.DateTimeField(auto_now_add = True)
    summ = models.CharField(max_length=255, blank=True)
    term = models.CharField(max_length=255, blank=True)
    rate = models.CharField(max_length=255, blank=True)
    product = models.CharField(max_length=255, blank=True)
    payVar = models.CharField(max_length=255, blank=True)
    loanSumm = models.CharField(max_length=255, blank=True)
    bank_bik = models.CharField(max_length=255, blank=True)
    bank_ls = models.CharField(max_length=255, blank=True)
