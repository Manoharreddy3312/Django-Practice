from django.urls import path
from.import views

urlpatterns = [ 
    path('', views.home,name='home'),
    path('display/', views.display , name='display'),
    path('single/<int:a>', views.single ,name='single'),
    path('history/',views.history,name = 'history'),
    path('about/',views.about,name = 'about'),
    path('edit/<int:b>', views.edit, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),

]