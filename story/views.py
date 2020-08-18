from django.shortcuts import render

def story(request):
    ''' function to render Mollys Story page'''

    return render (request, 'story/index.html')