from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import To_do




# Create your views here.

# @login_required
# def index(request):
#     return render(request, 'index.html')

@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        desc = request.POST.get('desc')
        if task:
            To_do.objects.create(task=task, desc=desc, user=request.user)
        return redirect('home')
    return render(request, 'index.html')


@login_required(login_url='login')

def display(request):
    data = To_do.objects.filter(user=request.user)
    context = {'data': data}
    return render(request, 'display.html',context)
