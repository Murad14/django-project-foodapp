from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisteForm

# Create your views here.

def register(req):
    if req.method == 'POST':
        form = RegisteForm(req.POST)
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(req,f'Welcome {username}, your account is created!')
           return redirect('food:index')
    else:
        form = RegisteForm()
    return render(req, 'users/register.html', {'form':form})


# abdnZ7*4D9hjWW2 murad
# F5FVik3n2-uNYS9 murad1