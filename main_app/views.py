from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegistrationForm


def index_view(request: WSGIRequest):
    return render(request, 'main_app/index.html')


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'main_app/registration.html'
    success_url = reverse_lazy('index')


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'main_app/login.html'
