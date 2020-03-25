from django.views.generic import ListView
from blog.models import Article

class FeaturedArticles(ListView):
    queryset = Article.objects.filter(featured=True).order_by('-created_at')
    context_object_name = 'articles'
    paginate_by = 1

    