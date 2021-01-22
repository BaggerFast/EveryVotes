import datetime
from django.contrib import messages
from application.forms import VotingForm, VoteForm
from application.models import Voting, VoteVariant
from application.views import *


class CreateVoteView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {
            'title': 'Create vote',
            'btn': 'Make',
            'count': 3,
        }

    def get(self, request):
        self.context['navbar'] = get_navbar(request)
        form = VotingForm()
        form_vote = VoteForm()
        VoteForm.create(form_vote, self.context['count'])
        self.context['form'] = form
        self.context['vote_variants'] = form_vote
        return render(request, Page.create_vote, self.context)

    def post(self, request):
        self.context['navbar'] = get_navbar(request)
        form = VotingForm(request.POST)
        form_of_votes = VoteForm(request.POST)
        if form.is_valid() and form_of_votes.is_valid():
            post = Voting.objects.create(
                author=request.user,
                title=form.data['title'],
                description=form.data['description'],
                publish_at=form.data['start_time'],
                finish_at=form.data['end_time'],
            )
            for i in range(self.context['count']):
                VoteVariant.objects.create(voting=post, description=form_of_votes.data[f'Vote variant {i+1}'])
            messages.success(request, 'A new post has been created!')
            return redirect(reverse('main'))
        else:
            messages.error(request, 'There is an error in the form!', extra_tags='danger')
        self.context['form'] = form
        VoteForm.create(form_of_votes, self.context['count'])
        self.context['vote_variants'] = form_of_votes
        return render(request, Page.create_vote, self.context)
