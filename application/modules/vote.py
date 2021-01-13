from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from application.models import Voting, VoteVariant, VoteFact
from application.views import *


@login_required
def vote_page(request, vote_id):
    View.current = View(request, 'Vote template', 'pages/vote.html')

    vote = get_object_or_404(Voting, id=vote_id)
    variants = vote.votevariant_set.all()
    facts = VoteFact.objects.filter(variant__voting=vote, author=request.user)
    facts_count = facts.count()

    View.current.context.update({
        'vote': vote,
        'variants': variants,
        'errors': [],
        'facts': facts,
    })

    if request.method == 'POST':
        variant_id = request.POST.get('action', None)

        if variant_id:
            fact_variant = get_object_or_404(VoteVariant, id=variant_id)

            if fact_variant.voting.id != vote_id:
                View.current.context['errors'].append('Нельзя голосовать за варианты другого голосования')
                return View.current.get_render_page()

            if facts_count > 0:
                View.current.context['errors'].append('Вы уже проголосовали')
                return View.current.get_render_page()

            fact = VoteFact(variant=fact_variant, author=request.user)
            fact.save()
        else:
            View.current.context['errors'].append('Не указаны детали голоса')
            return View.current.get_render_page()

    return View.current.get_render_page()
