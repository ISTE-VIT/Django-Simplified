from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def  home(request):
    return HttpResponse("Hello, World !")

def welcome(request):
    return HttpResponse("Welcome to this session on django !")

def greet(request):
    return HttpResponse("Hello, Vidyarth !")

def greet_name(request,name):
    return render(request,"hello.html",{
        "str" : name
    })