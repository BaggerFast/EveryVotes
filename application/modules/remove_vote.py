from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from application.models import Voting
from application.views import *


class RemoveVotePage(LoginRequiredMixin, View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {}

    def get(self, request, id):
        vote = get_object_or_404(Voting, id=id)
        vote.closed = True
        vote.save()
        messages.success(request, f'The vote {vote.title} remove!')
        return redirect(reverse('own_voting_list'))
