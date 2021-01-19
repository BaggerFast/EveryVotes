from django.shortcuts import render


class View:
    current = None

    def get_navbar(self):
        navbar = [{'url': 'main', 'label': 'Home'}]
        if self.request.user.is_authenticated:
            navbar += [
                {'url': 'create_vote', 'label': 'Create post'},
                {'url': 'voting_list', 'label': "GlobalVote"},
                {'url': 'own_voting_list', 'label': "OwnVote"},
                {'url': 'logout', 'label': "Logout"},
            ]
        else:
            navbar += [{'url': 'login', 'label': 'Login'},
                       {'url': 'registration', 'label': 'Registration'}]
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
