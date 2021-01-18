from django.shortcuts import render, redirect


class Url:
    admin = 'admin'
    main = ''
    vote = 'vote/<int:id>'
    login = 'login'
    logout = 'logout'
    registration = 'registration'
    create_vote = 'create_vote'
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
        self.context = dict()
        self.get_base_context()
        # self.get_messages()
        View.current = self

    def get_base_context(self):
        self.context['navbar'] = self.get_navbar()
        self.context['title'] = self.title
        # self.context['messages'] = []

    # def get_messages(self):
    #     self.context['messages'] = []
    #     if View.current:
    #         for message in View.current.context['messages']:
    #             if not message['viewed']:
    #                 self.context['messages'].append(message)
    #             message['viewed'] = True
    #
    # def push_message(alert: str, message: str, page: str):
    #     View.current.message({'alert': alert, 'message': message})
    #     return redirect(page)
    #
    # def message(self, message):
    #     message['viewed'] = False
    #     if not any(i['message'] == message['message'] for i in self.context['messages']):
    #         self.context['messages'].append(message)
    #     else:
    #         for i in range(len(self.context['messages'])):
    #             if self.context['messages'][i]['message'] == message['message']:
    #                 self.context['messages'][i]['viewed'] = False

    def get_render_page(self):
        return render(self.request, self.url, self.context)
