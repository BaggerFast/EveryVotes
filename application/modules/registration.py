from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User

from application.forms import RegistrationForm
from application.views import *


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
                    messages.success(request, 'New user has been registered successfully!')
                    return redirect('/' + Url.main)
                else:
                    messages.error(request, 'A user with this username already exists.', extra_tags='danger')
                    return redirect('/' + Url.registration)
            else:
                messages.error(request, 'Passwords are not the same', extra_tags='danger')
                return redirect('/' + Url.registration)
        else:
            messages.error(request, 'Form is not valid', extra_tags='danger')
            return redirect('/' + Url.registration)
    elif request.method == 'GET':
        View.current = View(request, 'registration', 'pages/registration.html')
        View.current.context['form'] = RegistrationForm()
    return View.current.get_render_page()
