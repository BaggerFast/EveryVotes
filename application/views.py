from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


def get_navbar(request):
    navbar = [{'url': 'main', 'label': 'Home'}]
    if request.user.is_authenticated:
        navbar += [
            {'url': 'create_vote', 'label': 'Create vote'},
            {'url': 'voting_list', 'label': "Global Vote"},
            {'url': 'own_voting_list', 'label': "Own Vote"},
            {'url': 'logout', 'label': "Logout"},
        ]
    else:
        navbar += [{'url': 'login', 'label': 'Login'},
                   {'url': 'registration', 'label': 'Registration'}]
    return navbar
