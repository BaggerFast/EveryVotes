from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from application.forms import VotingForm, VoteForm
from application.models import Voting, VoteVariant
from application.views import get_navbar, Page


class CreateVoteView(LoginRequiredMixin, View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {
            'title': 'Create vote',
            'btn': 'Make',
        }

    def get(self, request: WSGIRequest) -> HttpResponse:
        self.context['navbar'] = get_navbar(request)
        self.context['form'] = VotingForm()
        return render(request, Page.create_vote, self.context)

    def post(self, request: WSGIRequest) -> HttpResponse:
        self.context['navbar'] = get_navbar(request)
        if 'Vote variant 1' not in request.POST:
            form = VotingForm(request.POST)
            if form.is_valid():
                self.context['count'] = int(form.data['variant_count'])
                self.context['vote_variants'] = VoteForm.create(VoteForm(), self.context['count'])
            else:
                messages.error(request, 'There is an error in the form!', extra_tags='danger')
            self.context['form'] = form
        else:
            form_of_votes = VoteForm(request.POST)
            form = VotingForm(request.POST)
            if form_of_votes.is_valid():
                self.make_post(form, request)
                for i in range(int(request.POST['variant_count'])):
                    VoteVariant.objects.create(voting=self.post,
                                               description=form_of_votes.data[f'Vote variant {i + 1}'])
                messages.success(request, 'A new post has been created!')
                return redirect(reverse('main'))
            else:
                messages.error(request, 'There is an error in the form!', extra_tags='danger')
        return render(request, Page.create_vote, self.context)

    def make_post(self, form: VotingForm, request: WSGIRequest) -> None:
        self.post = Voting.objects.create(
            author=request.user,
            title=form.data['title'],
            description=form.data['description'],
            publish_at=form.data['start_time'],
            finish_at=form.data['end_time'],
        )
