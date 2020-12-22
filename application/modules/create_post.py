from application.views import *


def create_post_view(request):
    if request.method == 'POST':
        data = request.POST
        if request.user.is_authenticated:
            post = Voting(
                author=request.user,
                title=data['title'],
                description=data['description'],
            )
            post.save()
            View.current.push_message({'alert': 'success', 'message': 'A new post has been created!'})
            return redirect('/')
        else:
            View.current.push_message({'alert': 'danger', 'message': 'Oops, you are not logged in!'})
            return redirect('/create_post')
    elif request.method == 'GET':
        View.current = View(request, 'Create post', 'pages/create_post.html')
    return View.current.get_render_page()
