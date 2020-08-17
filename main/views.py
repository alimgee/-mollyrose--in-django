from django.shortcuts import render
from news.models import Article

def home(request):
    ''' function to render homepage'''
    article = Article.objects.last()
    context={
        'article':article
    }
    return render (request, 'main/index.html', context)

def about(request):
    ''' function to render homepage'''

    return render (request, 'main/about.html')
