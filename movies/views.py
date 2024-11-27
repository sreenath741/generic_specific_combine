from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def movie(request):
    return HttpResponse('<h1>salaar</h1>')

