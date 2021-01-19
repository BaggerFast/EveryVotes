from application.views import *
from application.models import Voting


class VoteListView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {
            'title': 'Votings',
            'navbar': None
        }

    def get(self, request):
        self.context['navbar'] = get_navbar(request)
        item = Voting.objects.all()
        for i in range(len(item)):
            item[i].check_settings()
        self.context['votings'] = Voting.objects.filter(closed=False)
        return render(request, 'pages/votings_list.html', self.context)

