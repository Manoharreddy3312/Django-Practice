from django.shortcuts import render, redirect
from .forms import AccountCreationForm , Recaptcha
from .models import Accounts
from django.core.mail import send_mail
from .utils.otp import otp
from django.conf import settings
# Create your views here.

def  index(request):
    return render(request,'index.html')


def acc_creation(request):
    form = AccountCreationForm()
    form1 = Recaptcha()
    if request.method == "POST":
        form = AccountCreationForm(request.POST,request.FILES)
        form1 = Recaptcha(request.POST)
        if form.is_valid() and form1.is_valid():
            form.save()
            print('added')
    context = {
        'form':form,
        'form1':form1
    }
    return render(request,"acc_creation.html",context)

def pin_gen(request):
    msg=""
    data=None
    if request.method=="POST":
        acc=int(request.POST.get('acc'))
        aadhar=int(request.POST.get('aadhar'))
        phone=int(request.POST.get('phone'))
        try:
            data=Accounts.objects.get(acc_num=acc)
        except:
            msg="Account doesn't Exist"
        
        if data:
            if data.aadhar==aadhar:
                if data.phone==phone:
                    b=otp()
                    send_mail(f"OTP is {b}","don't share your one time password with anyone and it will expire in 10mins",settings.EMAIL_HOST_USER,[data.email],fail_silently=True)
                    request.session['acc']=data.acc_num
                    request.session['opt']=b
                    return redirect('valid')
                else:
                    msg="phone number is not valid"
            else:
                msg="aadhar number mismatch"
    context={
        'msg':msg
    }
    return render(request,'pin_gen.html',context)

def validation(request):
    msg=""
    if request.method=="POST":
        opt=int(request.session['opt'])
        acc=int(request.session['acc'])
        otp=int(request.session['otp'])
        pin=int(request.session['pin'])
        c_pin=int(request.session['c_pin'])
        if otp==opt:
            if pin==c_pin:
                data=Accounts.objects.get(acc_num==acc)
                data.set_pin(str(pin))
                data.save()
                return redirect('home')
            else:
                msg="Pin missmatch"
        else:
            msg="OTP is invalid PLease Try again"
        #print(opt,acc)
    context={
        'msg':msg
    }
    return render(request,'valid.html',context)

def check_balance(request):
    msg=""
    data=None
    if request.method=="POST":
        acc=int(request.POST.get('acc'))
        pin=int(request.POST.get('pin'))


def pin_gen(request):
    msg=""
    data=None
    if request.method=="POST":
        acc=int(request.POST.get('acc'))
        aadhar=int(request.POST.get('aadhar'))
        phone=int(request.POST.get('phone'))
        try:
            data=Accounts.objects.get(acc_num=acc)
        except:
            msg="Account doesn't Exist"
        
        if data:
            if data.aadhar==aadhar:
                if data.phone==phone:
                    b=otp()
                    send_mail(f"OTP is {b}","don't share your one time password with anyone and it will expire in 10mins",settings.EMAIL_HOST_USER,[data.email],fail_silently=True)
                    request.session['acc']=data.acc_num
                    request.session['opt']=b
                    return redirect('valid')
                else:
                    msg="phone number is not valid"
            else:
                msg="aadhar number mismatch"
    context={
        'msg':msg
    }
    return render(request,'pin_gen.html)',context)

def deposit(request):
    data = None
    if request.method == "POST":
        acc = int(request.POST.get('acc'))
        pin = int(request.POST.get('pin'))
        amt = int(request.POST.get('amt'))
        try:
            data = Accounts.objects.get(acc_num=acc)
        except:
            message.error(request,"Account doesn't Exist","transition.html")

        if data:
            if int(data.get_pin()) == pin:
                data.balance >=100
                data.save()
