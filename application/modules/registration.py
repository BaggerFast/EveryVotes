from django.contrib.auth import login
from django.contrib.auth.models import User

from application.forms import RegistrationForm
from application.views import *
from django.shortcuts import redirect


def registration_view(request):
    if request.method == 'POST':
        data = request.POST
        form = RegistrationForm(data)
        if form.is_valid():
            if data['password'] == data['repeat_password']:
                user = User.objects.filter(username=data['username']).exists()
                if not user:
                    user = User.objects.create_user(
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        username=data['username'],
                        password=data['password'],
                    )
                    user.save()
                    login(request, user)
                    return View.push_message(alert='success', message='New user has been registered successfully!', page='/' + Url.main)
                else:
                    return View.push_message(alert='danger', message= 'A user with this username already exists.', page='/' + Url.registration)
            else:
                return View.push_message(alert='danger', message='Passwords don\'t same', page='/' + Url.registration)
        else:
            return View.push_message(alert='danger', message='Form is not valid', page='/' + Url.registration)
    elif request.method == 'GET':
        View.current = View(request, 'registration', 'pages/registration.html')
        View.current.context['form'] = RegistrationForm()
    return View.current.get_render_page()
