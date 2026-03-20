from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("1/", views.display, name="display"),
    path("single/<int:id>/", views.single, name="single"),
    path("update/<int:id>/", views.update, name="update"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("about/",views.about,name="about"),
    path("history/",views.history,name="history")
]