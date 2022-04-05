from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request


def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'lachlan'})


def home(request):
    return render(request, 'home.html')


def room(request):
    return render(request, 'room.html')
