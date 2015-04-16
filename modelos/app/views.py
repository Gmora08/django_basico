from django.shortcuts import render
from app.models import Especie, Pato
# Create your views here.

def quiero_patos(request):
	patos = Pato.objects.all()
	print request.user
	return render(request,"tus_patos.html",{"patos":patos})
