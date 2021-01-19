from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.urls import reverse

from application.forms import AuthenticateForm
from application.views import *


class LoginView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {}

    def get(self, request):
        self.context['navbar'] = get_navbar(request)
        self.context['form'] = AuthenticateForm()
        return render(request, 'pages/login.html', self.context)

    def post(self, request):
        self.context['navbar'] = get_navbar(request)
        data = request.POST
        form = AuthenticateForm(data)
        if form.is_valid():
            user = authenticate(
                username=data['username'],
                password=data['password'],
            )
            if user:
                login(request, user)
                messages.success(request, 'You have successfully logged in!')
                return redirect(reverse('main'))
            else:
                messages.error(request, 'Invalid username and password pair.', extra_tags='danger')
        else:
            messages.error(request, 'Invalid username and password pair.', extra_tags='danger')
        self.context['form'] = AuthenticateForm(data)
        return render(request, 'pages/login.html', self.context)
