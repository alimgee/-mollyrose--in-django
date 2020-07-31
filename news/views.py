from django.shortcuts import render
from .models import Article

def news(request):
    ''' function to render news page with news feed from db'''
    articles = Article.objects.all().order_by('-date')
    context={
        'articles':articles
    }
    return render (request, 'news/index.html', context)