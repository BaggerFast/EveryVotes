from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404

from application.models import Voting, VoteVariant, VoteFact
from application.views import *


@login_required
def vote_page(request, id):
    View.current = View(request, 'Vote template', 'pages/vote.html')
    vote = get_object_or_404(Voting, id=id)
    variants = vote.votevariant_set.all()
    vid = request.GET.get('vid', None)
    if vid:
        fact_variant = get_object_or_404(VoteVariant, id=vid)
        fact_count = VoteFact.objects.filter(variant=fact_variant, author=request.user).count()
        if fact_count > 0:
            raise Http404  # Todo: tell user that he has already made a choice
        if fact_variant.voting.id != id:
            raise Http404  # Todo: tell user that wrong variant has passed
        fact = VoteFact(variant=fact_variant, author=request.user)
        fact.save()
    facts = VoteFact.objects.filter(variant__voting=vote, author=request.user)
    View.current.context['vote'] = vote
    View.current.context['variants'] = variants
    View.current.context['facts'] = facts

    return View.current.get_render_page()
