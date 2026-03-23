from django.shortcuts import render

from Protected_api.settings import API_KEY
import requests
from django.conf import settings


# Create your views here.

def index(request):
    data = ""
    if request.method == "POST":
        city = request.POST.get("city")

        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.API_KEY}").json()
        print(data)

    context = {
        "data": data
    }
    

    return render(request, 'index.html', context)


