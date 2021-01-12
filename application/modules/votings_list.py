from application.views import *
from application.models import Voting


def votings_list_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse('index'))
    View.current = View(request, 'Votings', 'pages/votings_list.html')
    item = Voting.objects.all()
    for i in range(len(item)):
        item[i].check_settings()
    View.current.context['votings'] = Voting.objects.filter(closed=False)
    return View.current.get_render_page()
