from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News, Gallery, Category


def index(request):
    title = ''
    description = ''
    return render(request, 'index.html', {'title': title, 'description': description})


def about(request):
    title = 'About'
    description = ''
    return render(request, 'about.html', {'title': title, 'description': description})


def services(request):
    title = 'Services'
    description = ''
    return render(request, 'services.html', {'title': title, 'description': description})


def news_list(request):
    title = 'News List'
    description = ''
    news_list = News.objects.all()
    paginator = Paginator(news_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news_list.html', {'title': title, 'description': description, 'news_list': news_list,
                                              'paginator': paginator, 'page_obj': page_obj})


def news(request, pk):
    news = get_object_or_404(News, pk=pk)
    title = news.title
    description = news.description
    return render(request, 'news.html', {'title': title, 'description': description, 'news': news})


def projects(request):
    title = 'Projects'
    description = ''
    return render(request, 'projects.html', {'title': title, 'description': description})


def gos(request):
    title = 'Title'
    description = ''
    images_skolkovo = Gallery.objects.filter(category='1')
    return render(request, 'gos.html', {'title': title, 'description': description, 'images_skolkovo': images_skolkovo})


def infra(request):
    title = 'Title'
    description = ''
    images_infra = Gallery.objects.filter(category='1')
    return render(request, 'infra.html', {'title': title, 'description': description, 'images_infra': images_infra})


def prom(request):
    title = 'Title'
    description = ''
    return render(request, 'prom.html', {'title': title, 'description': description})


def jil(request):
    title = 'Title'
    description = ''
    return render(request, 'jil.html', {'title': title, 'description': description})


def torg(request):
    title = 'Title'
    description = ''
    return render(request, 'torg.html', {'title': title, 'description': description})


def admin(request):
    title = 'Title'
    description = ''
    return render(request, 'admin.html', {'title': title, 'description': description})


def vacancies(request):
    title = 'Vacancies'
    description = ''
    return render(request, 'vacancies.html', {'title': title, 'description': description})


def contact(request):
    title = 'Contact'
    description = ''
    return render(request, 'contact.html', {'title': title, 'description': description})

