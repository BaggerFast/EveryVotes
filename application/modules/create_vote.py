from django.contrib.auth.decorators import login_required
from application.forms import VotingForm
from application.models import Voting, VoteVariant
from application.views import *


@login_required
def create_vote_view(request):
    if request.method == 'POST':
        data = request.POST
        form = VotingForm(data)
        if form.is_valid():
            post = Voting(
                author=request.user,
                title=form.data['title'],
                description=form.data['description'],
                publish_at=form.data['start_time'],
                finish_at=form.data['end_time'],

            )
            post_variants = VoteVariant(
                voting=post,
                description=form.data['description1']
            )
            post.save()
            post_variants.save()
            post_variants = VoteVariant(
                voting=post,
                description=form.data['description2']
            )
            post_variants.save()
            View.current.context['form'] = form
            return View.push_message(alert='success', message='A new post has been created!', page='/' + Url.main)
        else:
            View.current.context['form'] = form
            return View.push_message(alert='danger', message='There is an error in the form!', page='/' + Url.create_vote)
    elif request.method == 'GET':
        View.current = View(request, 'Create vote', 'pages/create_vote.html')
        View.current.context['form'] = VotingForm()
    return View.current.get_render_page()