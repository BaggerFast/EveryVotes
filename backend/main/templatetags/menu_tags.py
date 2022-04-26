from django import template
from django.urls import reverse_lazy

from backend.utils import Navbar

register = template.Library()


@register.simple_tag
def get_menu(request):
    return Navbar(request).get()


@register.simple_tag
def off_current_url(request, url) -> str:
    if request.path == reverse_lazy(url):
        return 'disabled'
    return ''


@register.simple_tag
def compare_urls(request, url_name):
    return request.path == reverse_lazy(url_name)
