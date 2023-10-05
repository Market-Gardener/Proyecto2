from django.shortcuts import render
from django.http import HttpResponse
from AppIsaac.models import Pisina
from AppIsaac.form import userForm

def inicio(request):
    return render(request, "AppIsaac/base.html")

def pisina(request):
    return render(request, "AppIsaac/pisinas.html")

def items(request):
    return render(request, "AppIsaac/items.html")

def users(request):
    return render(request, "AppIsaac/users.html")

def pisinaForm(request):
    if request.method == 'POST':
        myForm = userForm(request.POST)
        print(myForm)
        
        if myForm.is_valid:
            pisina = Pisina (request.POST['pisina'], request.POST['price'])
            pisina.save()
            return render(request, "AppIsaac/base.html")
    else:
        myForm = userForm()
    
    return render(request, "AppIsaac/form.html", {"myForm": myForm})

def busquedaPisina(request):
    return render(request, "AppIsaac/busquedaPisina.html")

def buscar(request):
    if request.GET["price"]:
        #answer = f"Buscando precio de pisinas: {request.GET['price']}"
        price = request.GET['price']
        pisina = Pisina.objects.filter(price_icontains=price)
        
        return render(request, "AppIsaac/resultadoB.html", {"pisina": pisina, "price": price})
        
    else:
        answer = "no hay datos"
        
    
    return HttpResponse(answer)
    