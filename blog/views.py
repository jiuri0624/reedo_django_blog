import markdown
from markdown.extensions.toc import TocExtension
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import Article, Article, Category
# Create your views here.

def index(request):
    article_list = Article.objects.all()
    return render(request, 'blog/index.html', {'article_list': article_list})

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.increase_views()
    md = markdown.Markdown(extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     TocExtension(slugify=slugify),
                                  ])
    article.body = md.convert(article.body)
    article.toc = md.toc
    return render(request, 'blog/detail.html', {'article':article})

def archives(request, year, month):
    article_list = Article.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, 'blog/index.html', {'article_list': article_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(category=cate)
    return render(request, 'blog/index.html', {'article_list': article_list})