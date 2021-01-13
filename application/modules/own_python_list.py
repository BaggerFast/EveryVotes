from django.shortcuts import redirect
from django.urls import reverse

from application.views import *
from application.models import Voting


def own_votings_list_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse('index'))
    item = Voting.objects.all()
    for i in range(len(item)):
        item[i].check_settings()
    View.current = View(request, 'OwnVotings', 'pages/own_votings_list.html')
    View.current.context['active_votings'] = Voting.objects.filter(author=request.user, closed=False)
    View.current.context['closed_votings'] = Voting.objects.filter(author=request.user, closed=True)
    View.current.context['not_active_votings'] = Voting.objects.filter(author=request.user, visible=False)
    return View.current.get_render_page()
