from django.contrib import messages
from django.http import HttpResponseRedirect

from application.models import VoteFact, Voting
from application.views import *


class UserVotesList(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {}

    def get(self, request, author_id):
        self.context['navbar'] = get_navbar(request)
        if author_id:
            variants = list(Voting.objects.filter(author_id=author_id, closed=False).order_by("-created_at"))
            self.context['data'] = variants
            if request.user == variants[0].author:
                return redirect(reverse('own_voting_list'))
            if len(variants) == 0:
                messages.error(request, 'This user dont have active votes', extra_tags='danger')
                return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        return render(request, Page.user_votes, self.context)

