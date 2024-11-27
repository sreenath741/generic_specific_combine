from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def bike(request):
    return HttpResponse('my favourite bike is  ROYAL ENFIELD')
