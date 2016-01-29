from django.conf import settings
from goodmfo.models import UserInfo

def my_vars(request):
    user = request.user
    if user.is_authenticated():
        user_id = user.id
        client = UserInfo.objects.get(client_id=user_id)
        helloname = client.surname + ' ' + client.name
    return {
        'helloname': helloname,
    }