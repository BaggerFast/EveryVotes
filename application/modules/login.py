from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.urls import reverse

from application.forms import AuthenticateForm
from application.views import *


def login_view(request):
    if request.method == 'POST':
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
                return redirect(reverse('login'))
        else:
            messages.error(request, 'Invalid username and password pair.', extra_tags='danger')
            return redirect(reverse('login'))
    elif request.method == 'GET':
        Diew.current = Diew(request, 'Login', 'pages/login.html')
        Diew.current.context['form'] = AuthenticateForm()
    return Diew.current.get_render_page()
