from django.forms import ModelForm, MultipleChoiceField, ValidationError
from backend.voting.models import Voting


class CreateVariantsField(MultipleChoiceField):

    def validate(self, vote_variants: list):
        if len(vote_variants) > 6:
            raise ValidationError('Очень много вариантов голосований')
        if all(len(i) <= 20 for i in vote_variants):
            return
        raise ValidationError('Кол-во символов в голосовании <= 20')


class VotingForm(ModelForm):

    vote_variants = CreateVariantsField()

    class Meta:
        model = Voting
        exclude = ('author', 'date_created', 'closed')
