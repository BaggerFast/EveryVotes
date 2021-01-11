from django import forms


class CreateVotingForm(forms.Form):
    title = forms.CharField(
        label='Название',
        max_length=50,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'InputTitle',
                'v-model': 'title'
            }
        )
    )
    description = forms.CharField(
        label='Описание',
        max_length=255,
        widget=forms.Textarea(
            attrs={
                'rows': '3',
                'class': 'form-control',
                'id': 'InputDescription',
                'v-model': 'description'
            }
        )
    )
    start_time = forms.DateTimeField(
        label="Дата начала",
        widget=forms.DateInput(
            attrs={
                'type': 'datetime-local',
                'max': "2021-01-15T23:59",
                'class': 'form-control',
                'id': 'InputDateStart',
                'v-model': 'date_start'
            }
        )
    )
    end_time = forms.DateTimeField(
        label="Дата Окончания",
        widget=forms.DateInput(
            attrs={
                'type': 'datetime-local',
                'max': "2021-01-15T23:59",
                'class': 'form-control',
                'id': 'InputDateEnd',
                'v-model': 'date_end'
            }
        )
    )

