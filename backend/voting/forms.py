from django.forms import ModelForm, MultipleChoiceField, ValidationError
from backend.voting.models import Voting


class CreateVariantsField(MultipleChoiceField):

    def validate(self, value: list):
        if len(value) > 6:
            raise ValidationError('Очень много вариантов голосований')
        if all(len(i) <= 20 for i in value):
            return
        raise ValidationError('Кол-во символов в голосовании <= 20')


class VotingForm(ModelForm):
    vote_variants = CreateVariantsField()

    class Meta:
        model = Voting
        fields = ('title', 'description')
