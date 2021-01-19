from django.contrib import messages
from django.contrib.auth.decorators import login_required
from application.forms import VotingForm
from application.models import VoteVariant, Voting
from application.views import *


@login_required
def create_edit_vote_view(request, id):
    if request.method == 'POST':
        data = request.POST
        form = VotingForm(data)
        if form.is_valid():
            current_vote = Voting.objects.get(id=View.current.save_info)
            current_variant = VoteVariant.objects.filter(voting_id=current_vote)

            current_vote.title = form.data['title']
            current_vote.description = form.data['description']
            current_vote.publish_at = form.data['start_time']
            current_vote.finish_at = form.data['end_time']
            current_vote.save()

            current_variant[0].description = form.data['description1']
            current_variant[0].save()

            current_variant[1].description = form.data['description2']
            current_variant[1].save()

            View.current.context['form'] = form
            messages.success(request, 'A vote has been changed!')
            return redirect('/' + Url.main)
        else:
            View.current.context['form'] = form
            messages.error(request, 'There is an error in the form!', extra_tags='danger')
            return redirect('/' + Url.create_vote)
    elif request.method == 'GET':
        View.current = View(request, 'Create vote', 'pages/create_vote.html')
        View.current.save_info = id
        current_vote = Voting.objects.get(id=View.current.save_info)
        current_variant = VoteVariant.objects.filter(voting_id=current_vote)
        data = {
            'title': current_vote.title,
            'description': current_vote.description,
            'description1': current_variant[0].description,
            'description2': current_variant[1].description,
            'start_time': current_vote.publish_at,
            'end_time': current_vote.finish_at,
        }
        View.current.context['form'] = VotingForm(data)
    return View.current.get_render_page()
