from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from application.models import VoteFact
from application.views import get_navbar, Page


class UserList(LoginRequiredMixin, View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {}

    def get(self, request, id):
        self.context['navbar'] = get_navbar(request)
        if id != 0:
            variants = list(VoteFact.objects.filter(variant_id=id))
            self.context['data'] = variants
        return render(request, Page.user_list, self.context)

