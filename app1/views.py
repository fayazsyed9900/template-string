from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def firststring(request):
    return HttpResponse('<h1>it is my first string form</h1>')

def secondstring(request):
    return HttpResponse('<h1>it is my second string form</h1>')
 


def htmlfirst(request):
    return render(request,"first.html")