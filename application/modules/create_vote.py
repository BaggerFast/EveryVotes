import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from application.forms import VotingForm
from application.models import Voting, VoteVariant


class CreateVoteView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {
            'title': 'Create vote',
            'btn': 'Make',
        }

    def get(self, request):
        form = VotingForm(
            initial={
                'start_time': (datetime.datetime.now() + datetime.timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M"),
                'end_time': (datetime.datetime.now() + datetime.timedelta(days=2, hours=2)).strftime("%Y-%m-%dT%H:%M")
            }
        )
        form.fields['start_time'].widget.attrs['min'] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
        self.context['form'] = form
        return render(request, 'pages/create_vote.html', self.context)

    def post(self, request):
        form = VotingForm(request.POST)
        if form.is_valid():
            post = Voting.objects.create(
                author=request.user,
                title=form.data['title'],
                description=form.data['description'],
                publish_at=form.data['start_time'],
                finish_at=form.data['end_time'],
            )
            VoteVariant.objects.create(voting=post, description=form.data['description1'])
            VoteVariant.objects.create(voting=post, description=form.data['description2'])

            messages.success(request, 'A new post has been created!')
            return redirect(reverse('main'))
        else:
            messages.error(request, 'There is an error in the form!', extra_tags='danger')
        self.context['form'] = form
        return render(request, 'pages/create_vote.html', self.context)
