from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req):
    return HttpResponse('Hello World')

def item(req):
    return HttpResponse('<h1>This is an item view</h1>')