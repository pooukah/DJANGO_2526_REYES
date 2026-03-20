from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

def estudiants(request):
    llistaEst = Person.objects.filter(rol = "Estudiant")
    msg = {'msg': llistaEst}
    return render(request, 'main_page2.html', msg)

def profes(request):
    llistaPro = Person.objects.filter(rol = "Professor")
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
# CREATE (html hecho)
def person_form(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuaris')
    context = {"formulari":form}
    return render(request, 'form.html', context)
# UPDATE (html hecho)
def update_person(request, pk):
    person_id = Person.objects.get(id=pk)
    form = PersonForm(instance=person_id)

    if request.method == "POST":
        form = PersonForm(request.POST, instance=person_id)
        if form.is_valid():
            form.save()
            return redirect('usuaris')

    context = {"formulari":form}
    return render(request, 'form.html', context)
# DELETE ()
def delete_user(request, pk):
    person_id = Person.objects.get(id=pk)

    if request.method == "POST":
        person_id.delete()
        return redirect('usuaris')

    context = {'person':person_id}
    return render(request, 'deletePerson.html', context)