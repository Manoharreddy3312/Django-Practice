from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.index),
# ]

urlpatterns = [
    path('1', views.index,name='home'),
    path('display', views.display , name='display'),
    path('single/<int:a>', views.single ,name='single'),
    path('edit/<int:b>', views.edit, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),



   
]   