from django.http import Http404
from django.shortcuts import render

from News import num
from News.models import Article


def index(request):
    article_on_page = num.pages(Article.objects.all().filter(is_published=True))
    context = {
        'articles': article_on_page,
    }
    return render(request, 'News/index.html', context)


def news(request, id):
    article = Article.objects.get(pk=int(id))
    context = {
        'article': article,
    }
    return render(request, 'News/news.html', context)


def ajax(request, count):
    if request.is_ajax():
        article_on_page = num.pages(Article.objects.all().filter(is_published=True), int(count))
        context = {
            'article': article_on_page,
        }
        return render(request, 'News/ajax.html', context)
    else:
        raise Http404
