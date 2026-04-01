from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name ="home"),
    path('acc',views.acc_creation,name="acc"),
]