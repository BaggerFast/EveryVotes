from django.shortcuts import render, redirect


class Url:
    admin = 'admin'
    main = ''
    vote = 'vote/<int:id>'
    login = 'login'
    logout = 'logout'
    registration = 'registration'
    create_vote = 'create_vote'
    edit_vote = 'edit_vote/<int:id>'
    votings_list = 'votings_list'
    own_votings_list = 'own_votings_list'


class View:
    current = None

    def get_navbar(self):
        navbar = [{'url': Url.main, 'label': 'Home'}]
        if self.request.user.is_authenticated:
            navbar += [
                {'url': Url.create_vote, 'label': 'Create post'},
                {'url': Url.votings_list, 'label': "GlobalVote"},
                {'url': Url.own_votings_list, 'label': "OwnVote"},
                {'url': Url.logout, 'label': "Logout"},
            ]
        else:
            navbar += [{'url': Url.login, 'label': 'Login'},
                       {'url': Url.registration, 'label': 'Registration'}]
        return navbar

    def __init__(self, request, title, url):
        self.request = request
        self.title = title
        self.url = url
        self.save_info = 1
        self.context = dict()
        self.get_base_context()
        View.current = self

    def get_base_context(self):
        self.context['navbar'] = self.get_navbar()
        self.context['title'] = self.title

    def get_render_page(self):
        return render(self.request, self.url, self.context)
