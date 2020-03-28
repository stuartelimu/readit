from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avator = models.ImageField(upload_to='avators/')
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    image = models.ImageField(upload_to='articles/')
    body = models.TextField()
    tags = TaggableManager()
    featured = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article-detail', kwargs={
            'slug': self.slug,
        })


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f"Comment by {self.name} on {self.article}"