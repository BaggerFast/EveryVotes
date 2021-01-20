from application.views import *


class MainView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {
            'navbar': None
        }

    def get(self, request):
        self.context['navbar'] = get_navbar(request)
        return render(request, Page.main, self.context)

