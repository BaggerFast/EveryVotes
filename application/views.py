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


def make(page):
        return 'pages/' + page + '.html'


class Page:
    create_vote = make('create_vote')
    main = make('index')
    login = make('login')
    own_votings_list = make('own_votings_list')
    registration = make('registration')
    vote = make('vote')
    votings_list = make('votings_list')
