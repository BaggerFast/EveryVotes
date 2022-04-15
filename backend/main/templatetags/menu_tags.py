from django import template
from backend.utils import Navbar

register = template.Library()


@register.simple_tag
def get_menu(request):
    return Navbar(request).get()
