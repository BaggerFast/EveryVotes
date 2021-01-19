from django.contrib.auth import logout
from application.views import *


class LogoutView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        logout(request)
        return redirect(reverse('main'))





