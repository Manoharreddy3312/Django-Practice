from django.urls import path
from . import views

urlpatterns = [

    path('', views.husharu, name='home'),
    path('funtime/',views.husharu),
    path('djtillu/',views.djtillu),
    path('kik/',views.kik),
    path('don/',views.don)
   
]