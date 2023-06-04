from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def register(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(req,f'Welcome {username}, your account is created!')
           return redirect('food:index')
    else:
        form = UserCreationForm()
    return render(req, 'users/register.html', {'form':form})


# abdnZ7*4D9hjWW2 murad
# F5FVik3n2-uNYS9 murad1