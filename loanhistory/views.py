from django.shortcuts import render
from django.shortcuts import render_to_response
from loanhistory.models import Loan
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def loanhistory(request):
    return render_to_response('loanhistory.html', {'loans': Loan.objects.all()})