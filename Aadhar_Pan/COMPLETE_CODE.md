# Aadhar_Pan – Complete Project Code

Place static images in `static/images/`: `satyameva.png`, `uidai.png`, `gandhi.png`, `qr_code.png`

---

## 1. app/templates/index.html

```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Aadhaar Search</title>
<style>
*{box-sizing:border-box;}
body{font-family:Arial,sans-serif;background:#e8e8e8;margin:0;padding:20px;text-align:center;}
.search{margin:24px 0;}
.search input{padding:10px 14px;width:280px;font-size:16px;border:1px solid #ccc;}
.search button{padding:10px 24px;background:#0a66c2;color:#fff;border:none;cursor:pointer;font-size:16px;}
.container{margin-top:32px;display:flex;flex-direction:column;align-items:center;gap:32px;}

/* ----- AADHAAR CARD ----- */
.aadhar-wrap{display:flex;gap:24px;flex-wrap:wrap;justify-content:center;}
.aadhar-card{width:336px;min-height:212px;background:#fff;border-radius:4px;box-shadow:0 2px 12px rgba(0,0,0,0.15);overflow:hidden;text-align:left;}
.aadhar-top{display:flex;align-items:center;justify-content:space-between;padding:4px 8px 2px;}
.aadhar-logo-left{width:32px;height:32px;flex-shrink:0;object-fit:contain;}
.aadhar-top-center{flex:1;display:flex;flex-direction:column;align-items:center;margin:0 6px;}
.aadhar-tricolor{height:6px;width:100%;max-width:180px;background:linear-gradient(90deg,#ff9933 33%,#fff 33%,#fff 66%,#138808 66%);}
.aadhar-head{font-size:9px;color:#333;padding:2px 0 0;}
.aadhar-logo-right{width:36px;height:36px;flex-shrink:0;object-fit:contain;}
.aadhar-body{display:flex;gap:10px;padding:8px 12px;}
.aadhar-photo{width:99px;height:125px;border:1px solid #333;flex-shrink:0;object-fit:cover;}
.aadhar-details{flex:1;font-size:11px;line-height:1.35;}
.aadhar-details p{margin:2px 0;}
.aadhar-details b{font-weight:600;}
.aadhar-num-wrap{text-align:center;padding:6px 0;font-size:18px;font-weight:bold;letter-spacing:4px;}
.aadhar-tagline{text-align:center;font-size:10px;font-weight:bold;padding:4px 0 8px;color:#333;}
.aadhar-back .aadhar-tricolor{margin-bottom:0;}
.aadhar-back .aadhar-top{padding-bottom:4px;}
.aadhar-back h4{font-size:11px;margin:8px 12px 4px;}
.aadhar-back .addr{font-size:11px;margin:0 12px 8px;line-height:1.4;}
.aadhar-back .back-foot{display:flex;justify-content:space-between;align-items:center;padding:8px 12px;border-top:1px solid #ddd;}
.aadhar-back .back-foot .num-label{font-size:9px;}
.aadhar-back .back-foot .num-val{font-size:14px;font-weight:bold;letter-spacing:2px;}
.aadhar-back .qr-box{width:80px;height:80px;border:1px solid #ccc;display:flex;align-items:center;justify-content:center;font-size:8px;color:#999;}

/* ----- PAN CARD ----- */
.pan-card{width:336px;min-height:212px;position:relative;border:1px solid #7ba3c7;border-radius:4px;box-shadow:0 2px 12px rgba(0,0,0,0.12);overflow:hidden;text-align:left;}
.pan-gandhi-bg{position:absolute;inset:0;background-image:url('{% static "images/gandhi.png" %}');background-size:cover;background-position:center;opacity:0.12;pointer-events:none;}
.pan-card-inner{position:relative;z-index:1;min-height:212px;background:linear-gradient(160deg,rgba(212,232,247,0.85) 0%,rgba(232,242,250,0.9) 50%,rgba(212,232,247,0.85) 100%);display:flex;flex-direction:column;}
.pan-tag{background:#0d47a1;color:#fff;text-align:center;padding:4px 0;font-size:9px;letter-spacing:0.5px;}
.pan-title{text-align:center;padding:2px 0;font-size:10px;font-weight:bold;color:#0d47a1;}
.pan-body{display:flex;justify-content:space-between;align-items:flex-start;padding:10px 12px;gap:10px;}
.pan-info{flex:1;font-size:11px;}
.pan-info .pan-num{font-size:16px;font-weight:bold;letter-spacing:2px;margin-bottom:6px;}
.pan-info p{margin:3px 0;}
.pan-photo{width:95px;height:115px;border:1px solid #333;flex-shrink:0;object-fit:cover;}
.pan-right-col{display:flex;flex-direction:column;align-items:flex-end;}
.pan-sign-box{border:1px solid #5a8ab0;border-radius:2px;padding:4px 6px;margin-top:4px;background:rgba(255,255,255,0.6);min-width:90px;}
.pan-sign-line{width:100%;height:28px;border-bottom:1px solid #333;margin-bottom:2px;}
.pan-sign-label{font-size:8px;color:#333;}
.pan-sign-hindi{font-size:8px;color:#555;}
</style>
</head>
<body>
<h2>Aadhaar Search</h2>
<div class="search">
<form method="post">{% csrf_token %}
<input type="text" name="aadhar" placeholder="Enter 12-digit Aadhaar" maxlength="12" pattern="[0-9]*" inputmode="numeric">
<button type="submit">Search</button>
</form>
</div>

{% if data %}
<div class="container">
<div class="aadhar-wrap">
<!-- AADHAAR FRONT -->
<div class="aadhar-card">
<div class="aadhar-top">
<img src="{% static 'images/satyameva.png' %}" class="aadhar-logo-left" alt="Satyameva Jayate">
<div class="aadhar-top-center">
<div class="aadhar-tricolor"></div>
<div class="aadhar-head">Government of India</div>
</div>
<img src="{% static 'images/uidai.png' %}" class="aadhar-logo-right" alt="UIDAI">
</div>
<div class="aadhar-body">
{% if data.image %}<img src="{{ data.image.url }}" class="aadhar-photo" alt="Photo">{% endif %}
<div class="aadhar-details">
<p><b>Name:</b> {{ data.first_name }} {{ data.last_name }}</p>
<p><b>DoB:</b> {{ data.dob }}</p>
<p><b>Gender:</b> {{ data.gender }}</p>
<p><b>Father:</b> {{ data.father }}</p>
<p><b>Mobile:</b> {{ data.phone }}</p>
</div>
</div>
<div class="aadhar-num-wrap">{% if data.aadhar %}{{ data.aadhar|slice:":4" }} {{ data.aadhar|slice:"4:8" }} {{ data.aadhar|slice:"8:12" }}{% endif %}</div>
<div class="aadhar-tagline">मेरा आधार, मेरी पहचान</div>
</div>
<!-- AADHAAR BACK -->
<div class="aadhar-card aadhar-back">
<div class="aadhar-top">
<img src="{% static 'images/satyameva.png' %}" class="aadhar-logo-left" alt="Satyameva Jayate">
<div class="aadhar-top-center">
<div class="aadhar-tricolor"></div>
<div class="aadhar-head">Government of India</div>
</div>
<img src="{% static 'images/uidai.png' %}" class="aadhar-logo-right" alt="UIDAI">
</div>
<h4>Address</h4>
<p class="addr">{{ data.address }}, {{ data.city }}, {{ data.state }}</p>
<div class="back-foot">
<div>
<span class="num-label">Aadhaar No.</span><br>
<span class="num-val">{% if data.aadhar %}{{ data.aadhar|slice:":4" }} {{ data.aadhar|slice:"4:8" }} {{ data.aadhar|slice:"8:12" }}{% endif %}</span>
</div>
<div class="qr-box">{% if data.aadhar %}<img src="{% static 'images/qr_code.png' %}" style="width:70px;height:70px;" alt="QR">{% else %}QR{% endif %}</div>
</div>
</div>
</div>

<!-- PAN CARD -->
<div class="pan-card">
<div class="pan-gandhi-bg" aria-hidden="true"></div>
<div class="pan-card-inner">
<div class="pan-tag">Income Tax Department</div>
<div class="pan-title">Permanent Account Number (PAN)</div>
<div class="pan-body">
<div class="pan-info">
<div class="pan-num">{% if data.pan %}{{ data.pan }}{% endif %}</div>
<p><b>Name:</b> {{ data.first_name }} {{ data.last_name }}</p>
<p><b>Father's Name:</b> {{ data.father }}</p>
<p><b>Date of Birth:</b> {{ data.dob }}</p>
</div>
<div class="pan-right-col">
{% if data.image %}<img src="{{ data.image.url }}" class="pan-photo" alt="Photo">{% endif %}
<div class="pan-sign-box">
<div class="pan-sign-line"></div>
<span class="pan-sign-label">Signature</span><br>
<span class="pan-sign-hindi">हस्ताक्षर</span>
</div>
</div>
</div>
</div>
</div>
</div>
{% endif %}
</body>
</html>
```

---

## 2. app/views.py

```python
from django.shortcuts import render
from .forms import UserForm
from .models import User_Data


def index(request):
    data = None
    if request.method == "POST":
        aadhar = request.POST.get("aadhar")
        try:
            data = User_Data.objects.get(aadhar=aadhar)
        except:
            data = None
    return render(request, 'index.html', {'data': data})
```

---

## 3. app/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]
```

---

## 4. app/models.py

```python
from django.db import models


class Gender(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class User_Data(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    father = models.CharField(max_length=50)
    aadhar = models.CharField(max_length=12, unique=True, null=True, blank=True)
    pan = models.CharField(max_length=10, null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    dob = models.DateField()
    phone = models.PositiveIntegerField()
    address = models.TextField()
    city = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profiles')

    def __str__(self):
        return self.first_name
```

---

## 5. app/forms.py

```python
from django import forms
from .models import User_Data


class UserForm(forms.ModelForm):
    class Meta:
        model = User_Data
        fields = '__all__'
```

---

## 6. app/admin.py

```python
from django.contrib import admin
from .models import User_Data, Gender, State

admin.site.register(User_Data)
admin.site.register(Gender)
admin.site.register(State)
```

---

## 7. Aadhar_Pan/urls.py

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 8. Aadhar_Pan/settings.py (relevant parts)

Ensure these exist:

```python
INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
    'app',
]

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## Project structure

```
Aadhar_Pan/
├── Aadhar_Pan/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── app/
│   ├── templates/
│   │   └── index.html
│   ├── migrations/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/
│   └── images/
│       ├── satyameva.png   (Satyameva Jayate – Aadhaar top left)
│       ├── uidai.png       (UIDAI logo – Aadhaar top right)
│       ├── gandhi.png      (Gandhi – PAN background opacity)
│       └── qr_code.png     (optional – QR on Aadhaar back)
├── media/                  (uploaded profile photos)
├── manage.py
└── db.sqlite3
```

---

## Run

```bash
cd Aadhar_Pan
python manage.py runserver
```

Open http://127.0.0.1:8000/, enter a 12-digit Aadhaar, and click Search to see the cards.
