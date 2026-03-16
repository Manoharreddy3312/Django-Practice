from django.shortcuts import render,redirect
from .models import Todo_data
from .models import History_Table

# Create your views here.
def home(request):
    if request.method == 'POST':
        Task = request.POST.get('task')
        Description = request.POST.get('description')
        Todo_data.objects.create(Task = Task, Description = Description)
        return redirect('display')
    return render(request,'home.html')

# def history(request):
#     if request.method == 'POST':
#         Task = request.POST.get('task')
#         Description = request.POST.get('description')
#         return redirect('display')
#     return render(request,'history.html')


def display(request):
    data = Todo_data.objects.all().order_by('-id')
    context = {'data':data}
    return render(request,'display.html',context)

def single(request,a):
    data = Todo_data.objects.get(id=a)
    context = {'data':data}
    return render(request,'single.html',context)



def edit(request,b):
    data = Todo_data.objects.get(id=b)
    if request.method == 'POST':
        Task = request.POST.get('task')
        Description = request.POST.get('description')


        data.Task = Task
        data.Description = Description
        data.save()
        return redirect('display')
    

    context = {'data':data,'var':True}
    return render(request,'update.html',context)

   

# def history(request):
#     hist_data = History_Table.objects.all().order_by('-id')
#     return render(request, 'history.html', {'data': hist_data})

def history(request):
    data = History_Table.objects.all().order_by('-id')
    return render(request,'history.html',{'data':data})


def about(request):
    return render(request,'about.html')


def delete(request,id):
    data = Todo_data.objects.get(id=id)
    # ctrweate 
    History_Table.objects.create(Task = data.Task, Description = data.Description)
    data.delete()
    context = {'data':data}
    return redirect('history')
