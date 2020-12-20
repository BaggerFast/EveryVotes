from application.views import *


def registration_view(request):
    if request.method == 'POST':
        data = request.POST
        user = User.objects.filter(username=data['username']).exists()
        if not user:
            user = User.objects.create_user(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['username'],
                password=data['password']
            )
            user.save()
            login(request, user)
            View.current.push_message({'alert': 'success', 'message': 'New user has been registered successfully!'})
            return redirect('/')
        else:
            View.current.push_message({'alert': 'danger', 'message': 'A user with this username already exists.'})
            return redirect('/registration')
    elif request.method == 'GET':
        View.current = View(request, 'Registration', 'pages/registration.html')
    return View.current.get_render_page()
