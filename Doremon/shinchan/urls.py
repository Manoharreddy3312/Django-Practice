from django.urls import path
from . import views

urlpatterns = [
    path('',views.shinchan,name='shinchan'),


]