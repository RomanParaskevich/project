from rest_framework import viewsets
from blog.models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer


# Create your views here.
class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
