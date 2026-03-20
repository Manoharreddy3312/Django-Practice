from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('login')
    else:
        form = RegistrationForm()
    context = {'form': form}

    return render(request, 'register.html', context)

def log_in(request):
    msg = ''
    if request.method == 'POST':
        un = request.POST.get('un')
        pswd = request.POST.get('pswd')
        user = authenticate(request, username=un, password=pswd)
        if user is not None:
            login(request, user)
            return redirect('home')
        msg = 'Invalid credentials'
    return render(request, 'login.html', {'msg': msg})
def log_out(request):
    logout(request)
    return redirect('login')

            
