from django.shortcuts import render

# Create your views here.

def husharu(request):
    return render(request, 'husharu.html')

def djtillu(request):
    return render(request, 'djtillu.html')

def kik(request):
    return render(request, 'kik.html')

def don(request):
    return render(request, 'don.html')