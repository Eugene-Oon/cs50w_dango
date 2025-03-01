from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("Hello World!")
    # return HttpResponse("<h1 style=\"color:blue\">Hello World!</h1>")
    return render(request, "hello/index.html") # default in template folder alrdy

def brian(request):
    return HttpResponse("Hello Brian!")

def david(request):
    return HttpResponse("Hello David!")

def greet(request, name):
    # return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })