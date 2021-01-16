from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from application.forms import VotingForm
from application.models import Voting
from application.views import *


@login_required
def create_post_view(request):
    if request.method == 'POST':
        data = request.POST
        if request.user.is_authenticated:
            form = VotingForm(data)
            if form.is_valid():
                post = Voting(
                    author=request.user,
                    title=form.data['title'],
                    description=form.data['description'],
                    publish_at=form.data['start_time'],
                    finish_at=form.data['end_time']
                )
                post.save()
                View.current.push_message({'alert': 'success', 'message': 'A new post has been created!'})
                View.current.context['form'] = form
                return redirect(reverse('index'))
            else:
                View.current.context['form'] = form
                View.current.push_message({'alert': 'danger', 'message': 'There is an error in the form!'})
                return redirect(reverse('create_post'))
        else:
            View.current.push_message({'alert': 'danger', 'message': 'Oops, you are not logged in!'})
            return redirect(reverse('create_post'))
    elif request.method == 'GET':
        View.current = View(request, 'Create post', 'pages/create_post.html')
        View.current.context['form'] = VotingForm()
    return View.current.get_render_page()
