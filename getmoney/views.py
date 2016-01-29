from django.shortcuts import render

from django.template import Context
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from getmoney.models import PayVariant

@login_required(login_url='/login/')
def calculator(request):
    return render_to_response('getmoney.html', {'payvars': PayVariant.objects.all()})