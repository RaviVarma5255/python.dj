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


# next query parames ani vuntai avvi chudam
# qp :- antey :- thses r used to send extra information to d server without creating a new route

#  how to access it in jango

def info(request):
    name = request.GET.get('name','ravi') # :- ikada ravi annedi defalut value
    age = request.GET.get('age',0) #:- same 0 kuda defalut value
    data = {f'hello {name} , what your age , it was {age} mam'}
    return HttpResponse(data)

# ?name=varma&age=22 website lo ila access cheysukovali 