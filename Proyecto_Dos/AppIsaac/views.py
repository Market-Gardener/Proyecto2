from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "AppIsaac/index.html")

def pisina(request):
    return render(request, "AppIsaac/pisinas.html")

def items(request):
    return render(request, "AppIsaac/items.html")

def users(request):
    return render(request, "AppIsaac/users.html")
