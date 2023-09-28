from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola mundo")

def show_name(request, name):
    return HttpResponse("Bienvenido {{name}}")

def test_template(request):
    
    my_html = open('./Proyecto_Dos/plantillas/index.html')
    
    plantilla = Template(my_html.read())
    
    my_html.close()
    
    my_context = Context()
    
    documento = plantilla.render(my_context)
    
    return HttpResponse(documento)