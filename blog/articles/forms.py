from django import forms

from .models import Article, ArticleCategory

class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={"placeholder": "title"}))
    anons = forms.CharField(label='',
                            widget=forms.Textarea(attrs={"placeholder": "anons"}))
    full_text = forms.CharField(label='',
                            widget=forms.Textarea(attrs={"placeholder": "full text"}))
    image = forms.ImageField(required=False)
    class Meta:
        model = Article
        fields = [
            'title',
            'anons',
            'full_text',
            'articleCategory',
            'image'
        ]

class RawArticleForm(forms.Form):
    title           = forms.CharField(label='',
                                      widget=forms.TextInput(attrs={"placeholder": "title"}))
    anons           = forms.CharField(widget=forms.Textarea())
    full_text       = forms.CharField(widget=forms.Textarea())
    articleCategory = forms.ModelChoiceField(queryset=ArticleCategory.objects.all())
    image           = forms.ImageField(required=False)