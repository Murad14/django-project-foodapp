from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def index(req):
    item_list = Item.objects.all()
    return HttpResponse(item_list)



def item(req):
    return HttpResponse('<h1>This is an item view</h1>')