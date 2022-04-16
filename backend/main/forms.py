from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 15

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2',)
        labels = {'username': 'Логин', }
        help_texts = {
            "username": 'Не более 15 символов. Только буквы, цифры и символы @/./+/-/_.',
        }
