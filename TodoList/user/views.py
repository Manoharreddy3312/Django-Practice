from django.shortcuts import redirect, render
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
# Create your views here.
def register(request):
    form=RegistrationForm()
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("User Registered Successfully")
            return redirect("login")
    context={"form":form}
    return render(request, "register.html", context)

def log_in(request):
    msg=""
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        # print(f"Username: {username}, Password: {password}")
        try:
            a=User.objects.get(username=username)
        except Exception as e:
            msg=e
        if a:
            user=authenticate(request, username=username, password=password)
            print(f"Authenticated User: {user}")
            login(request,user)
            return redirect("home")
    context={'msg': msg}
    return render(request, "login.html", context)

def log_out(request):
    logout(request)
    return redirect("login")