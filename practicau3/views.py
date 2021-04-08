from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
# Create your views here.
def pagina(request):
    externo = open("C:/Users/NirusanMaerh/Documents/monicarojas/Template/index.html")
    plantilla = Template(externo.read())
    externo.close()
    ctx = Context()
    contenido = plantilla.render(ctx)
    return HttpResponse(contenido)


