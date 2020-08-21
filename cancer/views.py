from django.shortcuts import render

def cancer(request):
    ''' function to render childhood cancer page'''

    return render (request, 'cancer/index.html')

