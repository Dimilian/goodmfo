from django.shortcuts import render
from django.shortcuts import render_to_response


def loanhistory(request):
    return render_to_response('loanhistory.html')