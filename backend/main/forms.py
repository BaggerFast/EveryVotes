from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class BaseForm:
    fields = dict()

    def setup(self):
        for key in self.fields.keys():
            self.fields[key].widget.attrs['class'] = 'form-control'


class UserRegistrationForm(UserCreationForm, BaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup()
        self.fields['username'].widget.attrs['maxlength'] = 15

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2',)
        labels = {'username': 'Логин', }
        help_texts = {
            "username": 'Не более 15 символов. Только буквы, цифры и символы @/./+/-/_.',
        }
