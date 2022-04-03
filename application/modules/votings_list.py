from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from application.models import Voting
from application.views import get_navbar, Page


class VoteListView(LoginRequiredMixin, View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {
            'title': 'Votings',
        }

    def get(self, request):
        self.context['navbar'] = get_navbar(request)
        item = Voting.objects.all()
        for i in range(len(item)):
            item[i].check_settings()
        self.context['votings'] = Voting.objects.filter(closed=False).order_by("-created_at")
        return render(request, Page.votings_list, self.context)
