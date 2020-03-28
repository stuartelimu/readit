from django.contrib import admin

from .models import Article, Author, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Comment)

