from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from AppIsaac import Pisina

def saludo(request):
    return HttpResponse("Hola mundo")

def show_name(request, name):
    return HttpResponse("Bienvenido {{name}}")

def test_template(request):
    
    name = "Jose"
    last_name = "Lopez"
    diccionario = {"name": name, "ln": last_name, "grade": [5, 8, 3, 9, 1]}
    
    my_html = open('./Proyecto_Dos/plantillas/index.html')
    
    plantilla = Template(my_html.read())
    
    my_html.close()
    
    my_context = Context()
    
    documento = plantilla.render(my_context)
    
    return HttpResponse(documento)

def test_loader(request):
    diccionario = {
        "name": name,
        "last_name": ln,
        "notas": [5, 8, 3, 9, 1]
    }
    plantillas = loader.get_template('index.html')
    documento = plantillas.render(diccionario)
    return HttpResponse(documento)

def pisina(request, name, number):
    pool = Pisina(name = name, camada = int(number))
    pool.save()
    documento = f"Pisina: {pool.name}<br>Cloro: {pool.camada}"
    return HttpResponse(documento)