from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect

from goodmfo.forms import PersonalDataForm
from goodmfo.models import UserInfo
# Create your views here.

@login_required(login_url='/login/')
def index(request):
    return render_to_response('base.html', context={'request': request})


@login_required
def user_personal_data(request):
    if request.method == 'GET':
        client_form = PersonalDataForm(instance=request.user.userinfo)
    else:
        client_form = PersonalDataForm(
            data=request.POST,
            instance=request.user.userinfo,
        )
        if client_form.is_valid():
            client_form.save()
            return redirect('personal_data')
    return render_to_response(
        'user_info.html',
        {
            'request': request,
            'client_form': client_form
        }
    )
