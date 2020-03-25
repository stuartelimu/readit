from django.urls import path
from .views import ArticleList

app_name = 'blog'

urlpatterns = [
    path('blog/', ArticleList.as_view(), name='article-list'),
]