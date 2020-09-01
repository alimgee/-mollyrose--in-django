from django.shortcuts import render
from news.models import Article
from .models import Notice

def home(request):
    ''' function to render homepage and show first article
    and also allow a notice module to be displayed or not
    '''
    article = Article.objects.last()
    notice = Notice.objects.all()
    context={
        'article':article,
        'notice':notice
    }
    return render (request, 'main/index.html', context)

def about(request):
    ''' function to render homepage'''

    return render (request, 'main/about.html')
