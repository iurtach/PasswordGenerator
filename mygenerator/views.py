from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'mygenerator/home.html')

def password(request):


    characteres = list ('abcdefjklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characteres.extend(list('ABCDEFJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characteres.extend(list('!@#$%ˆ&*()_-+='))

    if request.GET.get('number'):
        characteres.extend(list('0123456789'))


    length = int(request.GET.get('length',12))

    thepassword =''

    for x in range(length):
        thepassword += random.choice(characteres)


    return render(request, 'mygenerator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'mygenerator/about.html')
