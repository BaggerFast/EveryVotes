from application.views import *


def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        data = request.POST
        user = authenticate(
            username=data['username'],
            password=data['password'],
        )
        if user:
            login(request, user)
            View.current.push_message({'alert': 'success', 'message': 'You have successfully logged in!'})
            return redirect('/')
        else:
            View.current.push_message({'alert': 'danger', 'message': 'Invalid username and password pair.'})
            return redirect('/login')
    elif request.method == 'GET':
        View.current = View(request, 'Login', 'pages/login.html')
    return View.current.get_render_page()
