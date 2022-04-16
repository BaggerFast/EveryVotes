from django.forms import ModelForm

from backend.voting.models import Voting


class VotingForm(ModelForm):

    class Meta:
        model = Voting
        exclude = ('author', 'date_created', 'closed')
