#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext #se utiliza para poder utilizar la ruta de los archivos estatic se debe poner en todas las funciones
# Seccion para la creación de las vistas que van a utilizar metodos
# para la localización de una escuela.
def localizarEs(request):
   html = "<html><body>Bienbenido a 'RECORDATORIO DE HORARIOS'</body></html>"
   return render_to_response('Login/inicioPagina.html',context_instance=RequestContext(request))