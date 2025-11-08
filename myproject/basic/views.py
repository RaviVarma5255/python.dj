from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("hello world !")

def add(request):
     a = 20
     b = 30
     c= a+b
     return HttpResponse(f"the sum of {a} and {b} is {c}")