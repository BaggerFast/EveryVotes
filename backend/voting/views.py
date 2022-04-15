from django.shortcuts import render
from django.views.generic import ListView, DetailView

from backend.voting.models import Voting


class VotingsView(ListView):
    model = Voting
    template_name = 'voting/voting_list.html'
    context_object_name = 'votings'
    extra_context = {'title': "Голосования"}

    def get_queryset(self):
        return self.model.objects.filter(closed=False)


class VotingView(DetailView):
    model = Voting
    template_name = 'voting/voting.html'
    extra_context = {'title': f"Голосование"}
