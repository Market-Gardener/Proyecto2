from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Vista Inicio")

def pisina(request):
    return HttpResponse("Vista Pisina")

def items(request):
    return HttpResponse("Vista Items")

def users(request):
    return HttpResponse("Vista Users")    
