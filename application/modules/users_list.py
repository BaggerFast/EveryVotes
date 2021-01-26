from django.contrib import messages
from django.http import HttpResponseRedirect
from application.models import VoteFact, Voting, VoteVariant
from application.views import *


class UsersList(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {}

    def get(self, request, variant_id):
        self.context['navbar'] = get_navbar(request)
        if variant_id:
            variants = list(VoteFact.objects.filter(variant_id=variant_id))
            self.context['data'] = variants
            if len(variants) == 0:
                messages.error(request, 'No user vote', extra_tags='danger')
                return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        return render(request, Page.user_list, self.context)

