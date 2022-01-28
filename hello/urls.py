
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="hello"),
    path("welcome/",views.welcome, name="welcome"),
    path("greet/",views.greet,name="vidyarth"),
    path("greet/<str:name>",views.greet_name,name="greet"),
]