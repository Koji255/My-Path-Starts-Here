from django.shortcuts import render
from django.http import HttpResponse

def sayHello(request):
    return HttpResponse("Hello, user!")

def sayHelloToUser(request):
    return render(request, 'helloToUser.html')

# Create your views here.