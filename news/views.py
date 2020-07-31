from django.shortcuts import render

def news(request):
    ''' function to render news page'''
    return render (request, 'news/index.html')