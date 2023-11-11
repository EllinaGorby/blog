from django.db import models


# Create your models here.
class ArticleCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=128)
    anons = models.TextField()
    full_text = models.TextField()
    articleCategory = models.ForeignKey(to=ArticleCategory, on_delete=models.PROTECT)
    views = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='article_images', null=True, blank=True)


    def __str__(self):
        return f'Article: {self.title} | Category: {self.articleCategory.name}'
