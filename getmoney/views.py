import json
import codecs

from django.shortcuts import render
import urllib2
# from urllib.request import  urlopen
from django.template import Context
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from getmoney.models import PayVariant, LoanProgram
from goodmfo.models import UserInfo
from loanhistory.models import Loan
from django.http import JsonResponse


@login_required(login_url='/login/')
def calculator(request):
    return render_to_response('getmoney.html', {'payvars': PayVariant.objects.all()})

@login_required(login_url='/login/')
def calculato(request):
    return render_to_response('loanhistory.html', {'payvars': PayVariant.objects.all()})

@login_required(login_url='/login/')
def payvar(request):
    reader = codecs.getreader("utf-8")
    payvar_data = json.load(reader(request))
    bank_ls = request.user.userinfo.bank_ls
    bank_bik = request.user.userinfo.bank_bik
    if (payvar_data['payvar'] == 'bank-balance'):
        return render_to_response('bank-balance.html', {'bank_ls': bank_ls, 'bank_bik': bank_bik})
    if (payvar_data['payvar'] == 'contact'):
        return render_to_response('contact.html')

@login_required(login_url='/login/')
def loan_submit(request):
    reader = codecs.getreader("utf-8")
    loan_data = json.load(reader(request))
    l = Loan()
    l.client_id = request.user.id
    l.summ = loan_data['summ']
    l.term = loan_data['term']
    l.rate = loan_data['rate']
    l.product = loan_data['program']
    l.loanSumm = loan_data['result']
    l.payVar = loan_data['payvar']
    l.save()
    return JsonResponse({'result':loan_data['summ']})

@login_required(login_url='/login/')
def calculate(request):
    # return JsonResponse({'foo': 'bar'})
    reader = codecs.getreader("utf-8")
    calculate_data = json.load(reader(request))
    # calculate_data = json.loads(response)
    program = LoanProgram.objects.filter(
        amount_from__lte=calculate_data['amount'],
        amount_to__gte=calculate_data['amount'],
        period_from__lte=calculate_data['days'],
        period_to__gte=calculate_data['days'],
        is_pensioner=calculate_data['is_pensioner'],
    ).first()
    if not program:

        return JsonResponse({'error': 'program_not_found'}, status=400)

    # TODO: CALCULATE ANNUITY
    result = calculate_data['amount'] + (calculate_data['amount'] * (program.rate/100)) * calculate_data['days']
    return JsonResponse({
        'total': result,
        'title': program.title,
        'rate': program.rate
    })
