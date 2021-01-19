from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse

from application.forms import VotingForm
from application.models import VoteVariant, Voting
from application.views import *


@login_required
def create_edit_vote_view(request, id):
    if request.method == 'POST':
        data = request.POST
        form = VotingForm(data)
        if form.is_valid():
            current_vote = Voting.objects.get(id=Diew.current.save_info)
            current_variant = VoteVariant.objects.filter(voting_id=current_vote)

            current_vote.title = form.data['title']
            current_vote.description = form.data['description']
            current_vote.publish_at = form.data['start_time']
            current_vote.finish_at = form.data['end_time']
            current_vote.save()

            for i in range(2):
                des = 'description' + str(i+1)
                current_variant[i].remake(form.data[des])

            Diew.current.context['form'] = form
            messages.success(request, 'A vote has been changed!')
            return redirect(reverse('main'))
        else:
            Diew.current.context['form'] = form
            messages.error(request, 'There is an error in the form!', extra_tags='danger')
            return redirect(reverse('create_vote'))
    elif request.method == 'GET':
        Diew.current = Diew(request, 'Create vote', 'pages/create_vote.html')
        Diew.current.save_info = id
        current_vote = Voting.objects.get(id=Diew.current.save_info)
        current_variant = VoteVariant.objects.filter(voting_id=current_vote)
        data = {
            'title': current_vote.title,
            'description': current_vote.description,
            'description1': current_variant[0].description,
            'description2': current_variant[1].description,
            'start_time': current_vote.publish_at.strftime("%Y-%m-%dT%H:%M"),
            'end_time': current_vote.finish_at.strftime("%Y-%m-%dT%H:%M"),
        }
        Diew.current.context['title'] = 'Edit vote'
        Diew.current.context['btn'] = 'Edit'
        Diew.current.context['form'] = VotingForm(data)
    return Diew.current.get_render_page()
