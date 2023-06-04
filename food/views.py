from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm



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
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item
    }
    return render(req,'food/detail.html',context)

def create_item(req):
    form = ItemForm(req.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(req, 'food/item-form.html', {'form':form})

def update_item(req, id):
    item = Item.objects.get(id=id)
    form = ItemForm(req.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(req,'food/item-form.html',{'form':form,'item':item})

def delete_item(req, id):
    item = Item.objects.get(id=id)

    if  req.method == 'POST':
       item.delete()
       return redirect('food:index')
    
    return render(req,'food/item-delete.html',{'item':item}) 

