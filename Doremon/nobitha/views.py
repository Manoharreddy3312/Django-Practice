from django.shortcuts import render

# Create your views here.
def doremon(request):
    return render(request,'doremon.html')

def nobitha(request):
    return render(request,'nobitha.html')

def shizuka(request):
    return render(request,'shizuka.html')

def suneo(request):
    return render(request,'suneo.html')

def geion(request):
    return render(request,'geion.html')

def dekisugi(request):
    return render(request,'dekisugi.html')