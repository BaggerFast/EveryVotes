from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from application.models import Voting, VoteVariant, VoteFact
from application.views import *


@login_required
def vote_page(request, id):
    View.current = View(request, 'Vote template', 'pages/vote.html')
    vote = get_object_or_404(Voting, id=id)
    variants = vote.votevariant_set.all()
    variant_id = request.GET.get('vid', None)
    facts = VoteFact.objects.filter(variant__voting=vote, author=request.user)
    View.current.context['facts'] = facts
    View.current.context['vote'] = vote
    View.current.context['variants'] = variants
    if variant_id:
        fact_variant = get_object_or_404(VoteVariant, id=variant_id)
        fact_count = VoteFact.objects.filter(variant__voting=vote, author=request.user).count()
        if fact_count > 0:
            messages.error(request, 'User has already made a choice.', extra_tags='danger')
            return redirect(reverse('vote', args=[id]))
        if fact_variant.voting.id != id:
            messages.error(request, 'Wrong variant has passed.', extra_tags='danger')
            return redirect(reverse('vote', args=[id]))
        fact = VoteFact(variant=fact_variant, author=request.user)
        fact.save()
        fact_variant_count = VoteFact.objects.filter(
            variant__voting=vote,
            variant__description=facts[0].variant.description
        ).count()
        View.current.context['variant_votes'] = fact_variant_count
    fact_total_count = VoteFact.objects.filter(variant__voting=vote).count()
    View.current.context['total_votes'] = fact_total_count
    return View.current.get_render_page()
