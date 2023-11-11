from django.shortcuts import render
from articles.models import Article, ArticleCategory
from django.http import HttpResponse


# Create your views here.
def home_views(request):
    context = {
        'title': 'Homepage',
    }
    return render(request, 'home1.html', context)


def about_views(request):
    context = {
        'title': 'about',
    }
    return render(request, 'about.html', context)
