from django.shortcuts import render
from .forms import UserForm
from .models import User_Data


def index(request):

    data = None

    if request.method == "POST":

        aadhar = request.POST.get("aadhar")

        try:
            data = User_Data.objects.get(aadhar=aadhar)
        except:
            data = None

    return render(request,'index.html',{'data':data})