from django import views
from django.shortcuts import render



def home(request):
    return render(request, 'store/home.html')

def mxplayer(request):
    return render(request, 'store/mxplayer.html')

def mobiles(request):
    return render(request, 'store/mobiles.html')

def bestsellers(request):
    return render(request, 'store/bestsellers.html')

def amazonpay(request):
    return render(request, 'store/amazonpay.html')

def fresh(request):
    return render(request, 'store/fresh.html')




