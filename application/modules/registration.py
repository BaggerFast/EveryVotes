from django.contrib.auth import login
from django.contrib.auth.models import User

from application.forms import RegistrationForm
from application.views import *
from django.shortcuts import redirect


def registration_view(request):
    if request.method == 'POST':
        data = request.POST
        form = RegistrationForm()
        if form.is_valid():
            user = User.objects.filter(username=data['username']).exists()
            if request.POST.password == request.POST.repeat_password:
                if not user :
                    user = User.objects.create_user(
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        username=data['username'],
                        password=data['password'],

                    )
                    user.save()
                    login(request, user)
                    View.current.push_message({'alert': 'success', 'message': 'New user has been registered successfully!'})
                    return redirect('/')
                else:
                    View.current.push_message({'alert': 'danger', 'message': 'A user with this username already exists.'})
                    return redirect('/registration')
            else:
                View.current.push_message({'alert': 'danger', 'message': 'Passwords don\'t match'})
                return redirect('/registration')
        else:
            View.current.push_message({'alert': 'danger', 'message': 'Form is not valid'})
            return redirect('/registration')
    elif request.method == 'GET':
        View.current = View(request, 'registration', 'pages/registration.html')
        View.current.context['form'] = RegistrationForm()
    return View.current.get_render_page()
