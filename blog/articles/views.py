from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from articles.models import Article, ArticleCategory
from django.urls import reverse

from .forms import ArticleForm

from django.views.generic import (
CreateView,
DeleteView,
ListView,
UpdateView,
DetailView
)

class ArticleListView(ListView):
    template_name = 'articles/articles_list.html'
    queryset = Article.objects.all()

def blog_views(request):
    context = {
        'title': 'blog',
        'articles': Article.objects.all(),
        'category': ArticleCategory.objects.all(),
    }
    return render(request, 'articles/blog.html', context)



def article_details_views(request, id):
    obj = get_object_or_404(Article, id=id)

    context = {
        'article': obj,
        'category': ArticleCategory.objects.all(),
    }
    return render(request, 'articles/article_details.html', context)


def article_add_views(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form = ArticleForm()
        return HttpResponseRedirect(reverse('blog:index'))
    context = {
        'form': form
    }
    return render(request, 'articles/article_add.html', context)

def article_delete_view(request, id): #TODO
    obj = get_object_or_404(Article, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse('blog:index'))

    context = {
        'article': obj
    }
    return render(request, 'articles/article_delete.html', context)