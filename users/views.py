from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisteForm

# Create your views here.

def register(req):
    if req.method == 'POST':
        form = RegisteForm(req.POST)
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(req,f'Welcome {username}, your are currently logged in!')
           return redirect('login')
    else:
        form = RegisteForm()
    return render(req, 'users/register.html', {'form':form})

@login_required
def profilepage(req):
    return render (req, 'users/profile.html')