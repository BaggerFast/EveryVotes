from application.views import *
from application.models import Voting


class VoteListView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {
            'title': 'Votings',
        }

    def get(self, request):
        self.context['navbar'] = get_navbar(request)
        item = Voting.objects.all()
        for i in range(len(item)):
            item[i].check_settings()
        self.context['votings'] = Voting.objects.filter(closed=False).order_by("-created_at")
        for i in range(len(self.context['votings'])):
            self.context['votings'][i].progress = int((self.context['votings'][i].finish_at - timezone.now()).seconds /
                                                      (self.context['votings'][i].finish_at - self.context['votings'][i].publish_at).seconds)
        return render(request, Page.votings_list, self.context)
