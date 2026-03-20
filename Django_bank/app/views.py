from django.shortcuts import render
from .forms import Acc_creationForm
from .models import Acc_creation

def index(request):
    if request.method == 'POST':
        form = Acc_creationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Best practice: redirect to a new URL to prevent form resubmission.
            # from django.shortcuts import redirect; return redirect('/success/')
            form = Acc_creationForm() # Show a new blank form after successful submission
    else:
        form = Acc_creationForm()
    return render(request, 'index.html', {'form': form})
