from django.views.generic import ListView, DetailView
from .models import Article
from taggit.models import Tag


class ArticleList(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/blog.html'
    paginate_by = 3


class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'blog/blog-single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.order_by("-created_at")[:3]
        context['tags'] = Tag.objects.all()
        return context