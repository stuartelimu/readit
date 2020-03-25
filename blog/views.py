from django.views.generic import ListView
from .models import Article


class ArticleList(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/blog.html'
    paginate_by = 3