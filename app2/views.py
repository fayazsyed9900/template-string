from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def string3(request):
    return  HttpResponse('<h1>this is app2 string form</h1>')


def string4(request):
        return  HttpResponse('<h1>this is app2 string form 2</h1>')

def htmlsecond(request):
    return render(request,"second.html")