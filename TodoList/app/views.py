from django.shortcuts import redirect, render
from .models import Todo_list  , History
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="login")
def home(request):
    if request.method=="POST":
        task=request.POST.get("task")
        description=request.POST.get("description")
        Todo_list.objects.create(user=request.user, task=task,description=description)
        print(task,description)
        print("data inserted successfully")
        return redirect("display")
    return render(request,"home.html")

@login_required(login_url="login")
def display(request):
    data=Todo_list.objects.filter(user=request.user).order_by("-id")
    context={
        "data":data
    }
    return render(request,"display.html",context)

@login_required(login_url="login")
def single(request,id):
    data=Todo_list.objects.get(user=request.user, id=id)
    context={
        "data":data
    }
    return render(request,"single.html",context)

@login_required(login_url="login")
def update(request,id):
    data=Todo_list.objects.get(user=request.user, id=id)
    if request.method=="POST":
        task=request.POST.get("task")
        description=request.POST.get("description")
        data.task=task
        data.description=description
        data.save()
        return redirect("display")
    context={
        "data":data ,
        "var": True
    }
    return render(request,"update.html",context)

@login_required(login_url="login")
def delete(request,id):
    data=Todo_list.objects.get(user=request.user, id=id)
    History.objects.create(task = data.task, description = data.description)
    data.delete()
    return redirect("display")

@login_required(login_url="login")
def history(request):
    data = History.objects.filter(user=request.user)
    context = {"data": data}
    return render(request,"history.html",context)

@login_required(login_url="login")
def about(request):
    return render(request,"about.html")