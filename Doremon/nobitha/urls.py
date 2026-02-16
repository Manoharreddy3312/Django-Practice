from django.urls import path
from . import views

urlpatterns = [
    path('doremon',views.doremon),
    path('nobitha',views.nobitha),
    path('shizuka',views.shizuka),
    path('suneo',views.suneo),
    path('geion',views.geion),
    path('dekisugi',views.dekisugi),
]
