from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from application.models import Voting
from application.views import get_navbar, Page


class OwnVoteListView(LoginRequiredMixin, View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {
            'title': 'OwnVotings',
            'btn': 'Make',
        }

    def get(self, request):
        self.context['navbar'] = get_navbar(request)
        item = Voting.objects.all()
        for i in range(len(item)):
            item[i].check_settings()
        self.context['active_votings'] = Voting.objects.filter(author=request.user, closed=False).order_by("-created_at")
        self.context['closed_votings'] = Voting.objects.filter(author=request.user, closed=True).order_by("-created_at")
        return render(request, Page.own_votings_list, self.context)
