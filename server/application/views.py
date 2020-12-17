from django.shortcuts import render

navbar = []


def base_page(url, title):
    context = {}
    navbar.append({'url': url, 'title': title})
    context['navbar'] = navbar
    context['title'] = title
    return context


def index_page(request):
    context = base_page('index', 'Главная')
    return render(request, 'pages/index.html', context)
