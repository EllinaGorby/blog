from django.contrib import admin

from .models import Article
from .models import ArticleCategory
# Register your models here.

admin.site.register(Article)
admin.site.register(ArticleCategory)