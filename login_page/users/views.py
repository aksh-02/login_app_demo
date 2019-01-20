from django.shortcuts import render, redirect
from .forms import UserSignup
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'users/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            form.save()
            # to authenticate the user once signup is done
            username = form.cleaned_data.get('username')
            pswd = form.cleaned_data.get('password1')
            messages.success(request, f'Thank You for Registration')
            user = authenticate(username=username, password=pswd)
            login(request, user)
            return redirect('home')
    else:
        form = UserSignup()
    return render(request, 'users/register.html', {'form' : form})