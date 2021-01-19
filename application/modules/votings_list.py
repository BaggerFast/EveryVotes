from django.contrib.auth.decorators import login_required
from application.views import *
from application.models import Voting


@login_required
def votings_list_view(request):
    Diew.current = Diew(request, 'Votings', 'pages/votings_list.html')
    item = Voting.objects.all()
    for i in range(len(item)):
        item[i].check_settings()
    Diew.current.context['votings'] = Voting.objects.filter(closed=False)
    return Diew.current.get_render_page()
