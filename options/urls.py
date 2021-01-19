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
from django.contrib.auth.decorators import login_required
from django.urls import path
from application.modules import *
from application.modules.create_vote import CreateVoteView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('admin/', admin.site.urls, name='admin'),

    path('login/', login_view, name='login'),
    path('logout/', login_required(LogoutView.as_view()), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),

    path('create_vote/', login_required(CreateVoteView.as_view()), name='create_vote'),
    path('voting_list/',  login_required(VoteListView.as_view()), name='voting_list'),
    path('own_voting_list/', login_required(OwnVoteListView.as_view()), name='own_voting_list'),

    path('vote/<int:id>/', vote_page, name='vote'),
    path('edit_vote/<int:cur_id>/', login_required(CreateEdiVoteView.as_view()), name='edit_vote'),
]
