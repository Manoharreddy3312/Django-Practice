# from django.shortcuts import render

from django.shortcuts import render
from .models import Mobiles


# Create your views here.

def cell(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        price = request.POST.get('price')
        battery = request.POST.get('battery')

        print(name, brand, price, battery)

        Mobiles.object.create(name=name, brand=brand, price=price, battery=battery)
    return render(request, 'display.html')

def display(request):
    data = Mobiles.objects.all().order_by('-id')
    
    context = {'data': data}
    return render(request, 'display.html',context)

