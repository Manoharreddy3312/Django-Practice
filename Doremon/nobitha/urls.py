
from django.urls import path
from . import views

urlpatterns = [
    path('',views.doremon,name='home'),
    path('nobitha',views.nobitha,name="nobitha"),
    path('shizuka',views.shizuka,name="shizuka"),
    path('suneo',views.suneo,name="suneo"),
    path('geion',views.geion,name="geion"),
    path('dekisugi',views.dekisugi,name = "dekisugi"),
]
