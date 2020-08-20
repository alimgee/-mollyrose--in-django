from django.shortcuts import render
from .models import Organisations


def help(request):
    ''' function to render homepage'''
    organisations = Organisations.objects.all().order_by('position')
    context ={
        'Organisations': organisations
    }

    return render (request, 'help/index.html', context)