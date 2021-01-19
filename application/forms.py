from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone


class VotingForm(forms.Form):
    title = forms.CharField(
        label='Title',
        max_length=50,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': 'form-control',
                'id': 'InputTitle',
                'v-model': 'title'
            }
        )
    )
    description = forms.CharField(
        label='Description',
        max_length=255,
        widget=forms.Textarea(
            attrs={
                'type': "text",
                'rows': '3',
                'class': 'form-control',
                'id': 'InputDescription',
                'v-model': 'description'
            }
        )
    )
    description1 = forms.CharField(
        label='Vote variant 1',
        max_length=20,
        widget=forms.Textarea(
            attrs={
                'type': "text",
                'rows': '1',
                'class': 'form-control',
                'id': 'InputDescription1',
                'v-model': 'description1'
            }
        )
    )
    description2 = forms.CharField(
        label='Vote variant 2',
        max_length=20,
        widget=forms.Textarea(
            attrs={
                'type': "text",
                'rows': '1',
                'class': 'form-control',
                'id': 'InputDescription2',
                'v-model': 'description2'
            }
        )
    )
    start_time = forms.DateTimeField(
        label="Start at",
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'max': "2021-01-30T23:59",
                'class': 'form-control',
                'id': 'InputDateStart',
                'v-model': 'date_start'
            }
        )
    )
    end_time = forms.DateTimeField(
        label="Finish at",
        widget=forms.DateInput(
            attrs={
                'type': 'datetime-local',
                'max': "2021-01-30T23:59",
                'class': 'form-control',
                'id': 'InputDateEnd',
                'v-model': 'date_end'
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('start_time') < timezone.now():
            raise ValidationError('Нельзя указывать дату в прошлом')


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label='First name',
        max_length=15,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': 'form-control',
                'id': 'InputFirstName',
                'v-model': 'first_name',
            }
        )
    )
    last_name = forms.CharField(
        label='Last name',
        max_length=15,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': 'form-control',
                'id': 'InputLastName',
                'v-model': 'last_name'
            }
        )
    )
    username = forms.CharField(
        label='Username',
        max_length=15,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': 'form-control',
                'id': 'InputUserName',
                'v-model': 'username'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        max_length=20,
        min_length=6,
        widget=forms.TextInput(
            attrs={
                'type': "password",
                'class': 'form-control',
                'id': 'InputPassword',
                'v-model': 'password'
            }
        )
    )
    repeat_password = forms.CharField(
        label='Repeat password',
        max_length=20,
        min_length=6,
        widget=forms.TextInput(
            attrs={
                'type': "password",
                'class': 'form-control',
                'id': 'InputRepeatPassword',
                'v-model': 'repeat_password'
            }
        )
    )


class AuthenticateForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=15,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': 'form-control',
                'id': 'InputUserName',
                'v-model': 'username'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        max_length=20,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                'type': "password",
                'class': 'form-control',
                'id': 'InputPassword',
                'v-model': 'password'
            }
        )
    )
