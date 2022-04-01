from django.shortcuts import render
from django.views import View
from application.views import get_navbar, Page


class MainView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {
            'navbar': None
        }

    def get(self, request):
        self.context['navbar'] = get_navbar(request)
        return render(request, Page.main, self.context)

