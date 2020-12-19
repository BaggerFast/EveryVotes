from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from application.models import Post


current_page = dict()

navbar = list()
navbar.append({'link': 'index', 'title': 'Home'})


def get_base_context(title):
    context = dict()
    context['navbar'] = navbar
    context['title'] = title
    context['messages'] = []
    return context


def get_page(data):
    return render(data['request'], data['url'], data['context'])


def index_page(request):
    global current_page
    context = get_base_context('Home')
    current_page = {
        'request': request,
        'url': 'pages/index.html',
        'context': context,
    }
    return get_page(current_page)


def login_view(request):
    global current_page
    if request.method == 'POST':
        data = request.POST
        user = authenticate(
            username=data['username'],
            password=data['password'],
        )
        if user:
            login(request, user)
            context = get_base_context('Home')
            current_page = {
                'request': request,
                'url': 'pages/index.html',
                'context': context
            }
            current_page['context']['auth_success'] = True
        else:
            current_page['context']['auth_success'] = False
    elif request.method == 'GET':
        context = get_base_context('Login')
        current_page = {
            'request': request,
            'url': 'pages/login.html',
            'context': context
        }
    return get_page(current_page)


def logout_view(request):
    global current_page
    logout(request)
    context = get_base_context('Home')
    current_page = {
        'request': request,
        'url': 'pages/index.html',
        'context': context,
    }
    return get_page(current_page)


def registration_view(request):
    global current_page
    if request.method == 'POST':
        data = request.POST
        user = User.objects.filter(username=data['username']).exists()
        if not user:
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            user.save()
            login(request, user)
            context = get_base_context('Home')
            current_page = {
                'request': request,
                'url': 'pages/index.html',
                'context': context,
            }
            current_page['context']['reg_success'] = True
        else:
            current_page['context']['reg_success'] = False
    elif request.method == 'GET':
        context = get_base_context('Registration')
        current_page = {
            'request': request,
            'url': 'pages/registration.html',
            'context': context,
        }
    return get_page(current_page)


def create_post_view(request):
    global current_page
    if request.method == 'POST':
        data = request.POST
        context = get_base_context('Home')
        if request.user.is_authenticated:
            post = Post(
                author=request.user.id,
                title=data['description'],
                created_at=datetime.now(),
            )
            post.save()
            context['messages'] = [{'alert': 'success', 'message': 'A new post has been created!'}]
        else:
            context['messages'] = [{'alert': 'danger', 'message': 'Oops, you are not logged in!'}]
        current_page = {
            'request': request,
            'url': 'pages/index.html',
            'context': context,
        }
    elif request.method == 'GET':
        context = get_base_context('Create post')
        current_page = {
            'request': request,
            'url': 'pages/create_post.html',
            'context': context,
        }
    return get_page(current_page)
