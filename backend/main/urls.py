from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import index_view, UserRegistrationView, UserLoginView


urlpatterns = [
    path('',  index_view, name='index'),
    path('logout/', login_required(LogoutView.as_view()), name='logout'),
    path('register/',  UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login')
]
