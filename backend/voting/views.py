from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from .forms import VotingForm
from .models import Voting, VoteVariant


class VotingsView(LoginRequiredMixin, ListView):
    model = Voting
    template_name = 'voting/voting_list.html'
    context_object_name = 'votings'
    extra_context = {'title': "Голосования"}

    def get_queryset(self):
        return Voting.objects.select_related('author').filter(closed=False).values('title', 'id', 'description',
                                                                                   'author__username')


class VotingView(LoginRequiredMixin, DetailView):
    model = Voting
    template_name = 'voting/voting.html'
    extra_context = {'title': f"Голосование"}


class CreateVotingView(LoginRequiredMixin, CreateView):
    form_class = VotingForm
    template_name = 'voting/create_voting.html'
    extra_context = {'title': f"Создать"}

    def form_valid(self, form: VotingForm) -> HttpResponseRedirect:
        voting: Voting = form.save(commit=False)
        voting.author = self.request.user
        voting.save()
        for variant_text in form.cleaned_data['vote_variants']:
            VoteVariant(voting=voting, title=variant_text).save()
        return HttpResponseRedirect(reverse_lazy('votings'))

