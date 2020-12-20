from application.views import *


def index_page(request):
    View.current = View(request, 'Home', 'pages/index.html')
    return View.current.get_render_page()
