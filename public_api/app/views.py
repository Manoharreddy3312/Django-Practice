from django.shortcuts import render
import requests



# Create your views here.

def index(request):
    data  = requests.get('https://restcountries.com/v3.1/all?fields=name,capital,currencies,flags').json()
    # print(data)
    if request.method == 'POST':
        con = request.POST.get('country')
        print(con)
        a = requests.get(f"https://restcountries.com/v3.1/name/{con}").json()
        print(a)
        
        return render(request, 'single.html',{'a': a})


    context = {'data': data}
    print(data)
    return render(request, 'index.html', context)

