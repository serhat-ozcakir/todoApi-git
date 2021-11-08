from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<center><h1 style = ''background-color:red;>Serhat</h1></center>')