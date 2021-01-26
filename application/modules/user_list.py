from django.contrib import messages
from django.http import HttpResponseRedirect

from application.models import VoteFact, Voting
from application.views import *


class UserList(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {}

    def get(self, request, author_id):
        self.context['navbar'] = get_navbar(request)
        if author_id != 0:
            variants = list(VoteFact.objects.filter().order_by("-created_at"))
            self.context['data'] = variants
            # if request == variants[0].author:
            #     return redirect(reverse('own_voting_list'))
        else:
            messages.error(request, 'No users', extra_tags='danger')
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        return render(request, Page.user_list, self.context)

