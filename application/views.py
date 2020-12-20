from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from application.models import Post


class View:
    navbar = list()
    navbar.append({'link': 'index', 'title': 'Home'})

    current = None

    def __init__(self, request, title, url):
        self.request = request
        self.title = title
        self.url = url
        self.context = dict()
        self.page = dict()
        self.get_base_context()
        self.get_messages()
        View.current = self

    def get_base_context(self):
        self.context['navbar'] = self.navbar
        self.context['title'] = self.title
        self.context['messages'] = []

    def get_messages(self):
        self.context['messages'] = []
        if View.current:
            for message in View.current.context['messages']:
                if not message['viewed']:
                    self.context['messages'].append(message)
                message['viewed'] = True

    def push_message(self, message):
        message['viewed'] = False
        if not any(i['message'] == message['message'] for i in self.context['messages']):
            self.context['messages'].append(message)
        else:
            for i in range(len(self.context['messages'])):
                if self.context['messages'][i]['message'] == message['message']:
                    self.context['messages'][i]['viewed'] = False

    def get_page(self):
        self.page = {
            'request': self.request,
            'url': self.url,
            'context': self.context,
        }
        return self.page

    def get_render_page(self):
        self.get_page()
        return render(self.page['request'], self.page['url'], self.page['context'])
