from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from application.models import Post

navbar = []


def base_page(url, title):
    context = {}
    navneed = True
    for navel in navbar:
        if navel['title'] == title:
            navneed = False
    if navneed:
        navbar.append({'url': url, 'title': title})
    context['navbar'] = navbar
    context['title'] = title
    return context


def index_page(request):
    context = base_page('index', 'Главная')
    return render(request, 'pages/index.html', context)


@csrf_exempt
def add_post(request):
    decryp = request.GET
    post = Post(title=decryp['title'])
    post.save()
    return render(request, 'pages/index.html')
