from django.urls import path
from . import views


urlpatterns = [
    path('mxhome', views.mxhome),
    path('newhot', views.newhot),
    path('webseries', views.webseries),
    path('movies', views.movies),
    path('vdesi', views.vdesi),
    path('romance', views.romance),
    path('comedy', views.comedy),
    path('tamil', views.tamil),
    path('telugu', views.telugu),

    
]