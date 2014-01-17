# Create your views here.
from django.shortcuts import render_to_response
from Publicaciones.models import *
#from django.http import HttpresponseRedirect
# from django.core.context_processsors import csrf

def home(request):
    # Recuperar 10 investigadores como minimo
    return render_to_response('base.html')

def investigadores(request):
    inv = Investigador.objects.all()[:10]
    return render_to_response('investigadores.html',{'investigadores':inv})
