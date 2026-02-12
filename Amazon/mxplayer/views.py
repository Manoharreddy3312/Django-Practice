from django.shortcuts import render

# Create your views here.


def mxhome(request):
    return render(request,'mxhome.html')

def newhot(request):
    return render(request,'newhot.html')

def webseries(request):
    return render(request,'webseries.html')

def movies(request):
    return render(request,'movies.html')

def vdesi(request):
    return render(request,'vdesi.html')

def romance(request):
    return render(request,'romance.html')

def comedy(request):
    return render(request,'comedy.html')

def tamil(request):
    return render(request,'tamil.html')

def telugu(request):
    return render(request,'telugu.html')

