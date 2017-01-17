from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest,HttpRequest
from blog.models import Articulo 
from django.core import serializers
import json

# Create your views here.


def index(request):
	pagina="index.html"

	return render(request,pagina)

def ajaxp(request):
	

	articulos=Articulo.objects.all()
	post_fields = (
        'titulo','cuerpo'
        
    )
	data=serializers.serialize('json', articulos,fields=post_fields)


	return HttpResponse(data, content_type="application/json")



def create(request):
	titulo2=request.POST.get('titulo3')
	cuerpo2=request.POST.get('cuerpo3')
	articulo2=Articulo(titulo=titulo2,cuerpo=cuerpo2)
	articulo2.save()
	articulo=Articulo.objects.filter(pk=articulo2.pk)
	
	data=serializers.serialize('json',articulo)

	

	return HttpResponse([data],content_type="application/json")


def inicio(request):
	pagina="inicio.html"
	return render(request,pagina)
	


