from django.urls import path
from .views import ArticleViewset, CommentViewset
from rest_framework.routers import DefaultRouter


urlpatterns = [

]

router = DefaultRouter()
router.register('articles', ArticleViewset)
router.register('comments', CommentViewset)
urlpatterns += router.urls
