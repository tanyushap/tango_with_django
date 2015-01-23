from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("<!DOCTYPE html> <html> <head> </head> <body><h1> This tutorial has been put together by Tanya Pavlova, 2068010p </h1> <br> <a href='/rango/index'>About</a></body></html>")#check if it works @home!!!!!!!
