from django import forms


class CreateVotingForm(forms.Form):
    title = forms.CharField(
        label='Название',
        max_length=255,
        min_length=4,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'exampleInputTitle',
                'v-model': 'title'
            }
        )
    )
    description = forms.CharField(
        label='Описание',
        max_length=255,
        widget=forms.Textarea(
            attrs={
                'rows': '4',
                'class': 'form-control',
                'id': 'exampleInputDescription',
                'v-model': 'description'
            }
        )
    )
