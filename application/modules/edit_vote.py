from django import forms
from django.contrib import messages
from application.forms import VotingForm, VoteForm
from application.models import VoteVariant, Voting
from application.views import *


def create_vote_variant(form, count):
    for i in range(len(count)):
        form.fields[f'Vote variant {i+1}'] = forms.CharField(
            initial=count[i].description,
            max_length=20,
            min_length=3,
            widget=forms.Textarea(
                attrs={
                    'rows': '1',
                    'class': 'form-control',
                }
            )
        )

def add_vote_variant(form, count):
    for i in range(count):
        form.fields[f'Vote variant {i+1}'] = forms.CharField(
            max_length=20,
            min_length=3,
            widget=forms.Textarea(
                attrs={
                    'rows': '1',
                    'class': 'form-control',
                }
            )
        )


class CreateEdiVoteView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {
            'title': 'Edit vote',
            'btn': 'Edit',
        }

    def get(self, request, cur_id):
        self.context['navbar'] = get_navbar(request)
        current_vote = Voting.objects.get(id=cur_id)
        current_variant = list(VoteVariant.objects.filter(voting_id=current_vote))
        self.context['title'] = 'Edit vote'
        self.context['btn'] = 'Edit'
        self.context['form'] = VotingForm(initial={
            'title': current_vote.title,
            'description': current_vote.description,
            'start_time': current_vote.publish_at.strftime("%Y-%m-%dT%H:%M"),
            'end_time': current_vote.finish_at.strftime("%Y-%m-%dT%H:%M")})
        form_vote = VoteForm()
        create_vote_variant(form_vote, current_variant )
        self.context['vote_variants'] =  form_vote
        return render(request,  Page.create_vote, self.context)

    def post(self, request, cur_id):
        self.context['navbar'] = get_navbar(request)
        data = request.POST
        form = VotingForm(data)
        form_of_votes = VoteForm(request.POST)
        self.context['form'] = form

        current_vote = Voting.objects.get(id=cur_id)
        current_variant = list(VoteVariant.objects.filter(voting_id=current_vote))

        if form.is_valid() and form_of_votes.is_valid():
            current_vote.title = form.data['title']
            current_vote.description = form.data['description']
            current_vote.publish_at = form.data['start_time']
            current_vote.finish_at = form.data['end_time']

            current_vote.save()

            for i in range(len(current_variant)):
                current_variant[i].remake(form_of_votes.data[f'Vote variant {i+1}'])

            messages.success(request, 'A vote has been changed!')
            return redirect(reverse('main'))
        else:
            messages.error(request, 'There is an error in the form!', extra_tags='danger')
        add_vote_variant(form_of_votes, len(current_variant))
        self.context['vote_variants'] = form_of_votes
        return render(request,  Page.create_vote, self.context)
