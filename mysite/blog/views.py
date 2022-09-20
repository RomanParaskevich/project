from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article, Comment


# Create your views here.
def articles(request):
    a = Article.objects.all()
    context = {
        'articles': a
    }
    return render(request, 'articles.html', context)


def article(request, slug):
    a = Article.objects.get(slug=slug)
    b = Comment.objects.filter(article=a.id)
    context = {
        'article': a,
        'comments': b
    }
    return render(request, 'article.html', context)


@login_required
def header_name_filter(request):
    if request.method == 'GET':
        header_name = request.GET.get('search_name')
        f = None
        if header_name:
            f = Article.objects.filter(header=header_name)
        context = {
            'articles': f
        }
    return render(request, 'header_name_filter.html', context)
