from django.db import models

# Create your models here.


class PayVariant(models.Model):
    payvar_name = models.CharField(max_length=100)
    payvar_title = models.CharField(max_length=100)
    payvar_icon = models.CharField(max_length=100, default='note_add')
    is_active = models.BooleanField(default=False)

class LoanProgram(models.Model):
    title = models.CharField(max_length=255)
    amount_from = models.BigIntegerField(default=0)
    amount_to = models.BigIntegerField(default=0)
    period_from = models.SmallIntegerField()
    period_to = models.SmallIntegerField()
    rate = models.FloatField()
    is_pensioner = models.BooleanField(default=False)

