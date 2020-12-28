from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>The home of my blog is here.</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1>")
