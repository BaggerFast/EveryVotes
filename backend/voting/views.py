from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import VotingForm
from .models import Voting


class VotingsView(LoginRequiredMixin, ListView):
    model = Voting
    template_name = 'voting/voting_list.html'
    context_object_name = 'votings'
    extra_context = {'title': "Голосования"}

    def get_queryset(self):
        return self.model.objects.filter(closed=False)


class VotingView(LoginRequiredMixin, DetailView):
    model = Voting
    template_name = 'voting/voting.html'
    extra_context = {'title': f"Голосование"}


class CreateVotingView(LoginRequiredMixin, CreateView):
    form_class = VotingForm
    template_name = 'voting/create_voting.html'
    extra_context = {'title': f"Создать"}

    def form_valid(self, form: VotingForm) -> HttpResponseRedirect:
        obj: Voting = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy('votings'))

