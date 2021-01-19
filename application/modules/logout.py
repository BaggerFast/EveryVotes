from django.contrib.auth import logout
from django.shortcuts import redirect

from application.views import *


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/' + Url.main)
