from application.models import VoteFact
from application.views import *


class UserList(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {}

    def get(self, request, id):
        self.context['navbar'] = get_navbar(request)
        if id != 0:
            variants = list(VoteFact.objects.filter(variant_id=id))
            self.context['data'] = variants
        return render(request, Page.user_list, self.context)

