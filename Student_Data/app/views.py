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

         Student_Db.objects.create(name=name,email=email,phone=mobile,dob=dob,qualification=qual,stream=stream,gender=gender)
    return render(request,'index.html')


def dispaly(request):
    data = Student_Db.objects.all().order_by('-id')
    context = {'data':data}
    return render(request,'display.html',context)
