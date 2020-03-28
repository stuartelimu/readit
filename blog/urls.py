from django.urls import path
from .views import ArticleList, ArticleDetail, CommentCreate

app_name = 'blog'

urlpatterns = [
    path('blog/', ArticleList.as_view(), name='article-list'),
    path('blog/<slug:slug>/', ArticleDetail.as_view(), name='article-detail'),
    path('blog/<slug:slug>/comment/', CommentCreate.as_view(), name='add-comment')
]