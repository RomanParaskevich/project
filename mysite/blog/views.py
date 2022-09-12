from django.shortcuts import render
from .models import Article, Comment


# Create your views here.
def articles(request):
    a = Article.objects.all()
    context = {
        'articles': a
    }
    return render(request, 'articles.html', context)


def article(request, article):
    a = Article.objects.get(header=article)
    b = Comment.objects.filter(article=a.id)
    context = {
        'article': a,
        'comments': b
    }
    return render(request, 'article.html', context)
