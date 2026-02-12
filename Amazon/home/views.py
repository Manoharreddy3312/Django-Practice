from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home.html')

def fresh(request):
    return render(request, 'fresh.html')




