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
            'count': None,
            'vote_variants': None
        }

    def get(self, request):
        self.context['navbar'] = get_navbar(request)
        #if self.context['count']:
        form = VotingForm()
        #form_vote = VoteForm()
        self.context['form'] = form
        #self.context['vote_variants'] = form_vote
        return render(request, Page.create_vote, self.context)

    def post(self, request):
        self.context['navbar'] = get_navbar(request)

        if not self.context['vote_variants']:
            form = VotingForm(request.POST)
            if form.is_valid():
                self.context['count'] = int(form.data['variant_count'])
                self.make_post(form, request)
                #messages.success(request, 'A new post has been created!')
                form_of_votes = VoteForm()
                VoteForm.create(form_of_votes, self.context['count'])
                self.context['vote_variants'] = form_of_votes
                return render(request, Page.create_vote, self.context)
            else:
                messages.error(request, 'There is an error in the form!', extra_tags='danger')
        else:
            form_of_votes = VoteForm(request.POST)
            if form_of_votes.is_valid():
                for i in range(self.context['count']):
                    VoteVariant.objects.create(voting=self.post, description=form_of_votes.data[f'Vote variant {i + 1}'])
                self.context['vote_variants'] = 'YES'
            else:
                messages.error(request, 'There is an error in the form!', extra_tags='danger')
        self.context['form'] = VotingForm(request.POST)
        # VoteForm.create(form_of_votes, self.context['count'])
        return render(request, Page.create_vote, self.context)

    def make_post(self, form, request):
        self.post = Voting.objects.create(
            author=request.user,
            title=form.data['title'],
            description=form.data['description'],
            publish_at=form.data['start_time'],
            finish_at=form.data['end_time'],
        )
