from django.shortcuts import render


def help(request):
    ''' function to render homepage'''

    return render (request, 'help/index.html')