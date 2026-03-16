from django.shortcuts import render
from .forms import SchorlarShipForm

# Create your views here.   


def index(request):
    form = SchorlarShipForm()
    if request.method == 'POST':
        form = SchorlarShipForm(request.POST)
        if form.is_valid():
            form.save()
        print('SAVED')

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)   


