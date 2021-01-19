from application.views import *
from application.models import Voting


class OwnVoteListView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {
            'title': 'OwnVotings',
            'btn': 'Make',
            'navbar': None
        }

    def get(self, request):
        self.context['navbar'] = get_navbar(request)
        item = Voting.objects.all()
        for i in range(len(item)):
            item[i].check_settings()
        self.context['active_votings'] = Voting.objects.filter(author=request.user, closed=False)
        self.context['closed_votings'] = Voting.objects.filter(author=request.user, closed=True)
        return render(request, 'pages/own_votings_list.html', self.context)


