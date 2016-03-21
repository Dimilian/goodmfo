

def mfo_processor(request):
    if not request.user.is_authenticated:
        return
    return {
        # 'user_info': request.user.userinfo,
    }
