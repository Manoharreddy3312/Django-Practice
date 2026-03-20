from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AccountForm, PinForm, BalanceForm
from .models import Account


def home(request):
    return render(request,'home.html')


def create_account(request):

    if request.method == "POST":
        form = AccountForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)

    else:
        form = AccountForm()

    return render(request,'create_account.html',{'form':form})


def set_pin(request):

    if request.method == "POST":

        form = PinForm(request.POST)

        if form.is_valid():

            acc = form.cleaned_data['account_number']
            pin = form.cleaned_data['pin']

            user = Account.objects.get(account_number=acc)
            user.pin = pin
            user.save()

            return render(request,'set_pin_success.html')
        

    else:
        form = PinForm()

    return render(request,'set_pin.html',{'form':form})


def balance(request):

    bal = None

    if request.method == "POST":

        form = BalanceForm(request.POST)

        if form.is_valid():

            acc = form.cleaned_data['account_number']
            pin = form.cleaned_data['pin']

            try:
                user = Account.objects.get(account_number=acc, pin=pin)
                bal = user.balance

            except:
                bal = "Invalid Details"

    else:
        form = BalanceForm()

    return render(request,'balance.html',{'form':form,'balance':bal})