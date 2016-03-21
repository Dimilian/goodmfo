from django.contrib import admin
from getmoney.models import PayVariant
from goodmfo.models import UserInfo
from getmoney.models import LoanProgram

# Register your models here.
admin.site.register(PayVariant)
admin.site.register(UserInfo)
admin.site.register(LoanProgram)