from application.views import *
from application.models import Voting


def own_votings_list_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse('main'))
    View.current = View(request, 'OwnVotings', 'pages/votings_list.html')
    View.current.context['votings'] = Voting.objects.filter(author=request.user)
    return View.current.get_render_page()
