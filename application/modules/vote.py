from django.contrib import messages
from django.shortcuts import get_object_or_404
from application.models import Voting, VoteVariant, VoteFact
from application.views import *


class VotePage(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {}

    def get(self, request, id):
        self.context['navbar'] = get_navbar(request)
        vote = get_object_or_404(Voting, id=id)
        self.context['cur_var'] = VoteFact.objects.filter(variant__voting=vote, author=request.user)
        self.context['vote'] = vote
        variants = list(VoteVariant.objects.filter(voting=vote))
        self.context['variants'] = variants
        data = []
        variant_id = request.GET.get('vid', None)
        if variant_id:
            fact_variant = get_object_or_404(VoteVariant, id=variant_id)
            fact_count = VoteFact.objects.filter(variant__voting=vote, author=request.user).count()
            fact = VoteFact(variant=fact_variant, author=request.user)
            fact.save()
            if fact_count > 0:
                messages.error(request, 'User has already made a choice.', extra_tags='danger')
            if fact_variant.voting.id != id:
                messages.error(request, 'Wrong variant has passed.', extra_tags='danger')
        for var in variants:
            a = VoteFact.objects.filter(variant=var).count()
            data.append((var, a))
        self.context['data'] = data
        return render(request, Page.vote, self.context)
