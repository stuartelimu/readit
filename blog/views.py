from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Article, Comment
from .forms import CommentForm
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
        # list of active comments for this particular article
        # self.get_object() - get this particular object
        context['comments'] = self.get_object().comments.filter(active=True)
        # add form 
        context['form'] = CommentForm()
        return context



class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('blog:article-detail', kwargs={
            'slug': self.object.article.slug
        })

    def form_valid(self, form):
        article = get_object_or_404(Article, slug=self.kwargs['slug'])
        form.instance.article = article
        return super().form_valid(form)
