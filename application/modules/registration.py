from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from application.forms import RegistrationForm
from application.views import *


class RegistrationView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {}

    def get(self, request):
        self.context['navbar'] = get_navbar(request)
        self.context['form'] = RegistrationForm()
        return render(request, Page.registration, self.context)

    def post(self, request):
        self.context['navbar'] = get_navbar(request)
        data = request.POST
        if RegistrationForm(data).is_valid():
            if data['password'] == data['repeat_password']:
                user = User.objects.filter(username=data['username']).exists()
                if not user:
                    user = User.objects.create_user(
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        username=data['username'],
                        password=data['password'],
                    )
                    login(request, user)
                    messages.success(request, 'New user has been registered successfully!')
                    return redirect(reverse('main'))
                else:
                    messages.error(request, 'A user with this username already exists.', extra_tags='danger')
            else:
                messages.error(request, 'Passwords are not the same', extra_tags='danger')
        else:
            messages.error(request, 'Form is not valid', extra_tags='danger')
        self.context['form'] = RegistrationForm(data)
        return render(request, Page.registration, self.context)
