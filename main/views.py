from django.shortcuts import render

def home(request):
    ''' function to render homepage'''
    return render (request, 'main/index.html')
