from django.shortcuts import render
from .models import Person

def estudiants(request):
    llistaEst = Person.objects.filter(rol = "EST")
    msg = {'msg': llistaEst}
    return render(request, 'main_page2.html', msg)

def profes(request):
    llistaPro = Person.objects.filter(rol = "PRO")
    print(llistaPro)
    msg = {'msg': llistaPro}
    return render (request, 'main_page2.html', msg)

def all(request):
    getAll = Person.objects.all()
    response = {"msg":getAll}
    return render(request, 'main_page.html', response)

def unUsuari(request, pk):
    getUserById = Person.objects.get(id=pk)
    response = {"msg": [getUserById]}
    return render(request, 'main_page2.html', response)