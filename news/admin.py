from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'date',
        'provider',
    )

admin.site.register(Article, ArticleAdmin)
