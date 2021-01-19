from django.contrib.auth.decorators import login_required
from application.views import *
from application.models import Voting


@login_required
def own_votings_list_view(request):
    item = Voting.objects.all()
    for i in range(len(item)):
        item[i].check_settings()
    Diew.current = Diew(request, 'OwnVotings', 'pages/own_votings_list.html')
    Diew.current.context['active_votings'] = Voting.objects.filter(author=request.user, closed=False)
    Diew.current.context['closed_votings'] = Voting.objects.filter(author=request.user, closed=True)
    return Diew.current.get_render_page()
