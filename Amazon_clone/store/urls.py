from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mxplayer/', views.mxplayer, name='mxplayer'),
    path('mobiles/', views.mobiles, name='mobiles'),
    path('bestsellers/', views.bestsellers, name='bestsellers'),
    path('amazonpay/', views.amazonpay, name='amazonpay'),
    path('fresh/', views.fresh, name='fresh')


]
