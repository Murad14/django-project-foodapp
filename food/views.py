from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.

def index(req):
    item_list = Item.objects.all()
    # template = loader.get_template('food/index.html')
    context = {
        'item_list': item_list,
    }
    # return HttpResponse(template.render(context,req))
    # Alternative way below
    return render(req,'food/index.html',context)




def item(req):
    return HttpResponse('<h1>This is an item view</h1>')

def detail(req,item_id):

    return HttpResponse(f"This is item no/id: {item_id}")
