from django.contrib import messages
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
                messages.success(request, 'You have successfully logged in!')
                return redirect('/' + Url.main)
            else:
                messages.error(request, 'Invalid username and password pair.', extra_tags='danger')
                return redirect('/' + Url.login)
        else:
            messages.error(request, 'Invalid username and password pair.', extra_tags='danger')
            return redirect('/' + Url.login)
    elif request.method == 'GET':
        View.current = View(request, 'Login', 'pages/login.html')
        View.current.context['form'] = AuthenticateForm()
    return View.current.get_render_page()
