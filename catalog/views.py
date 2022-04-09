from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("HOME")

def products(request):
    return HttpResponse("PRODUCTS")

def costumer(request):
    return HttpResponse("costumer")