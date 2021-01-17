from django.contrib.auth import login, authenticate
from application.forms import AuthenticateForm
from application.views import *


def login_view(request):
    if request.method == 'POST':
        data = request.POST
        form = AuthenticateForm(data)
        if form.is_valid():
            user = authenticate(
                username=data['username'],
                password=data['password'],
            )
            if user:
                login(request, user)
                return View.push_message(alert='success', message='You have successfully logged in!', page='/' + Url.main)
            else:
                return View.push_message(alert='danger', message='Invalid username and password pair.', page='/' + Url.login)
        else:
            return View.push_message(alert='danger', message='Invalid username and password pair.', page='/' + Url.login)
    elif request.method == 'GET':
        View.current = View(request, 'Login', 'pages/login.html')
        View.current.context['form'] = AuthenticateForm()
    return View.current.get_render_page()
