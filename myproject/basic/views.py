from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection

def home(request):
    return HttpResponse("hello world !")

def add(request):
     a = 20
     b = 30
     c= a+b
     return HttpResponse(f"the sum of {a} and {b} is {c}")

def health(request):

    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        return JsonResponse({"status":"ok","db":"connected"})
    
    except Exception as e:
        return JsonResponse({"status":"error","db":str(e)})
               


#  iddi mundu classes oka codes 

def cal(request):
    a='ravi'
    b='varma'
    c=a+b
    return HttpResponse(f"{c} is the name of me")