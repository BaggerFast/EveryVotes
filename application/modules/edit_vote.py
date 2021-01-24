from django.contrib import messages
from application.forms import VotingForm, VoteForm
from application.models import VoteVariant, Voting
from application.views import *


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
        variants_count = VoteVariant.objects.filter(voting_id=current_vote).count()
        self.context['title'] = 'Edit vote'
        self.context['btn'] = 'Edit'
        self.context['form'] = VotingForm(initial={
            'title': current_vote.title,
            'description': current_vote.description,
            'variant_count': variants_count,
            'start_time': current_vote.publish_at.strftime("%Y-%m-%dT%H:%M"),
            'end_time': current_vote.finish_at.strftime("%Y-%m-%dT%H:%M")})
        return render(request,  Page.edit_vote, self.context)

    def post(self, request, cur_id):
        self.context['navbar'] = get_navbar(request)
        if 'Vote variant 1' not in request.POST:
            form = VotingForm(request.POST)
            self.context['form'] = form
            if form.is_valid():
                current_vote = Voting.objects.get(id=cur_id)
                current_variants = list(VoteVariant.objects.filter(voting_id=current_vote))
                self.context['vote_variants'] = VoteForm.create(VoteForm(), len(current_variants), current_variants)
            else:
                messages.error(request, 'There is an error in the form!', extra_tags='danger')
        else:
            current_vote = Voting.objects.get(id=cur_id)
            current_variant = list(VoteVariant.objects.filter(voting_id=current_vote))
            form = VotingForm(request.POST)
            vote_variants= VoteForm(request.POST)
            if form.is_valid() and vote_variants.is_valid():
                current_vote.title = form.data['title']
                current_vote.description = form.data['description']
                current_vote.publish_at = form.data['start_time']
                current_vote.finish_at = form.data['end_time']
                current_vote.save()
                for i in range(len(current_variant)):
                    current_variant[i].remake(vote_variants.data[f'Vote variant {i + 1}'])
                messages.success(request, 'A vote has been changed!')
                return redirect(reverse('main'))
            else:
                messages.error(request, 'There is an error in the form!', extra_tags='danger')
        return render(request,  Page.edit_vote, self.context)
