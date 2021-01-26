from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from application.models import Voting, VoteVariant, VoteFact
from application.views import *


class VotePage(LoginRequiredMixin, View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {}

    def get(self, request, id):
        variant_id = request.GET.get('vid', None)
        self.context['navbar'] = get_navbar(request)
        vote = get_object_or_404(Voting, id=id)
        self.context['cur_var'] = VoteFact.objects.filter(variant__voting=vote, author=request.user)
        self.context['vote'] = vote
        variants = list(VoteVariant.objects.filter(voting=vote))
        if variant_id:
            fact_variant = get_object_or_404(VoteVariant, id=variant_id)
            fact_count = VoteFact.objects.filter(variant__voting=vote, author=request.user).count()
            if fact_count == 0:
                fact = VoteFact(variant=fact_variant, author=request.user)
                fact.save()
            else:
                messages.error(request, 'User has already made a choice.', extra_tags='danger')
        self.context['variants'] = variants
        data = []
        for var in variants:
            a = VoteFact.objects.filter(variant=var).count()
            data.append((var, a))
        self.context['data'] = data
        return render(request, Page.vote, self.context)
