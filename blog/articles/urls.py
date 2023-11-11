
from django.urls import path

import articles
from .views import ArticleListView, article_details_views, article_add_views, article_delete_view

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    # path('', blog_views, name='index'),
    path('<int:id>', article_details_views, name='details'),
    path('<int:id>/delete', article_delete_view, name='article_delete'),
    path('add', article_add_views, name='add'),

   ]