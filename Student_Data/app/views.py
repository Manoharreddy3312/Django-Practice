from django.shortcuts import render,redirect
from.models import Student_Db

# Create your views here.

def index(request):
    if request.method == 'POST':
         name = request.POST.get('name')
         email = request.POST.get('email')
         mobile = request.POST.get('mobile')
         dob = request.POST.get('DOB')
         qual = request.POST.get("qualification")
         stream = request.POST.get("stream")
         gender = request.POST.get("gender")

         print(name,email,mobile,dob,qual,stream,gender)

         Student_Db.objects.create(name=name,email=email,mobile=mobile,dob=dob,qualification=qual,stream=stream,gender=gender)
    return render(request,'index.html')


def display(request):
    data = Student_Db.objects.all().order_by('-id')
    context = {'data':data}
    return render(request,'display.html',context)

def single(request,a):
    data = Student_Db.objects.get(id=a)
    context = {'data':data}
    return render(request,'single.html',context)

def edit(request,b):
    data = Student_Db.objects.get(id=b)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        dob = request.POST.get('DOB')
        qual = request.POST.get("qualification")
        stream = request.POST.get("stream")
        gender = request.POST.get("gender")

        data.name = name
        data.email = email
        data.mobile = mobile
        data.dob = dob
        data.qualification = qual
        data.stream = stream
        data.gender = gender
        data.save()
        return redirect('display')
    

    context = {'data':data,'var':True}
    return render(request,'update.html',context)


def delete(request,id):
    data = Student_Db.objects.get(id=id).delete()
    return redirect('display')




