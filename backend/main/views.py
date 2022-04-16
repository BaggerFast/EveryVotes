from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegistrationForm


def index_view(request: WSGIRequest):
    return render(request, 'main/index.html', {'title': 'Главная'})


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'main/registration.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        user = authenticate(username=form.data.get('username'), password=form.data.get('password2'))
        login(self.request, user)
        return redirect(self.success_url)


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'
