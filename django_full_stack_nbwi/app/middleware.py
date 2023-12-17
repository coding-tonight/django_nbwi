# from django.shortcuts import redirect 
# from django.conf import settings

def auth(request):
    if request.user.is_authenticated:
        return True
    else:
        return  False