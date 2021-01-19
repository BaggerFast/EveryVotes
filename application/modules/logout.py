from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(reverse('main'))
