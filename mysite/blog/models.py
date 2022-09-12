from django.db import models


# Create your models here.
class Article(models.Model):
    header = models.CharField(max_length=100)
    text = models.TextField()


class Comment(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
