"""options URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application.modules import *
from application.views import Url

urlpatterns = [
    path(Url.main, index_page, name=Url.main),
    path(Url.vote + '/', vote_page, name='vote'),
    path(Url.admin + '/', admin.site.urls, name=Url.admin),
    path(Url.login + '/', login_view, name=Url.login),
    path(Url.logout + '/', logout_view, name=Url.logout),
    path(Url.registration + '/', registration_view, name=Url.registration),
    path(Url.create_vote + '/', create_vote_view, name=Url.create_vote),
    path(Url.votings_list + '/', votings_list_view, name=Url.votings_list),
    path(Url.own_votings_list + '/', own_votings_list_view, name=Url.own_votings_list),
]
