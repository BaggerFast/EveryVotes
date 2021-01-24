import datetime

from django import forms
from django.core.exceptions import ValidationError
from application.models import Voting
from django.utils import timezone


class FormTemplates:
    password = forms.CharField(
        max_length=20,
        min_length=6,
        widget=forms.TextInput(
            attrs={
                'type': "password",
                'class': 'form-control',
            }
        )
    )
    registration_text = forms.CharField(
        max_length=15,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': 'form-control',
            }
        )
    )


class VotingForm(forms.Form):
    title = forms.CharField(
        max_length=50,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    description = forms.CharField(
        max_length=255,
        widget=forms.Textarea(
            attrs={
                'rows': '3',
                'class': 'form-control',
            }
        )
    )
    variant_count = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'type': 'number',
                'value': 2,
                'min': 2,
                'max': 5,
            }
        )
    )
    start_time = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'value': (datetime.datetime.now() + datetime.timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M"),
                'min': (datetime.datetime.now() + datetime.timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M"),
                'max': (datetime.datetime.now() + datetime.timedelta(days=14)).strftime("%Y-%m-%dT%H:%M"),
                'class': 'form-control',
            }
        )
    )
    end_time = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'value': (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M"),
                'min': (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M"),
                'max': (datetime.datetime.now() + datetime.timedelta(days=14, minutes=10)).strftime("%Y-%m-%dT%H:%M"),
                'class': 'form-control',
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('start_time') < timezone.now():
            raise ValidationError('Нельзя указывать дату в прошлом')
        if cleaned_data.get('end_time') < cleaned_data.get('start_time'):
            raise ValidationError('Start time > End time, trying self-repair...')
        if Voting.objects.filter(title=cleaned_data.get('title', closed=True)).exists():
            raise ValidationError('Post with same title already exists!')


class RegistrationForm(forms.Form):
    first_name = FormTemplates.registration_text
    last_name = FormTemplates.registration_text
    username = FormTemplates.registration_text
    password = FormTemplates.password
    repeat_password = FormTemplates.password


class AuthenticateForm(forms.Form):
    username = FormTemplates.registration_text
    password = FormTemplates.password


class VoteForm(forms.Form):
    @staticmethod
    def create(form, count, data=[]):
        for i in range(count):
            form.fields[f'Vote variant {i + 1}'] = forms.CharField(
                max_length=20,
                min_length=3,
                widget=forms.Textarea(
                    attrs={
                        'rows': '1',
                        'class': 'form-control',
                    }
                )
            )
        if data:
            for i in range(len(data)):
                form.fields[f'Vote variant {i + 1}'].initial=data[i].description
        return form

    def clean(self):
        fields_keys = [key for key in self.data.keys() if key.startswith('Vote variant')]
        for key in fields_keys:
            if 3 > len(self.data.get(key)) or 20 < len(self.data.get(key)):
                raise ValidationError('Слишком длинный голос')
