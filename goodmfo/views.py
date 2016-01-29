from django.shortcuts import render_to_response
from goodmfo.models import UserInfo
# Create your views here.
def index(request):
    user = request.user
    if user.is_authenticated():
        user_id = user.id
        client = UserInfo.objects.get(client_id=user_id)
        helloname = client.surname + ' ' + client.name
    return render_to_response('base.html', {'helloname': helloname})

def userinfo(request):
    return render_to_response('userinfo.html', {'client': UserInfo.objects.all()})