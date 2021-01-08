from application.views import *


def vote_page(request):
    View.current = View(request, 'Vote template', 'pages/vote.html')
    return View.current.get_render_page()
