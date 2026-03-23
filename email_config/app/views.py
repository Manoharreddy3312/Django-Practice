from django.shortcuts import render , HttpResponse
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name') 
        email = request.POST.get('email')
        text = request.POST.get('text')
        # print(name, email, text)
        send_mail('thanks for your query',f'Hi {name},\n,{text}\nThank you for  reaching out to us. We have received your query and will get back to you shortly.',settings.EMAIL_HOST_USER,[email],fail_silently=True)  
        return HttpResponse('Email Sent Successfully..')
            
    return render(request, 'index.html')
