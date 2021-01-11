from application.views import *
from application.models import Voting


def votings_list_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse('main'))
    View.current.context['votings'] = Voting.objects.all()
    View.current = View(request, 'Votings', 'pages/votings_list.html')
    return View.current.get_render_page()
