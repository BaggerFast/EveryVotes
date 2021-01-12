from django.shortcuts import get_object_or_404

from application.models import Voting
from application.views import *


def vote_page(request, id):
    View.current = View(request, 'Vote template', 'pages/vote.html')
    vote = get_object_or_404(Voting, id=id)
    variants = vote.votevariant_set.all()
    View.current.context['vote'] = vote
    View.current.context['variants'] = variants
    return View.current.get_render_page()
