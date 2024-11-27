from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def car(request):
    return HttpResponse('my favourite car is  BMW')