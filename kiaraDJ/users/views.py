from django.shortcuts import render

def estudiants(request):
    llistaEstudiants = {
        'estudiant 1':{
            'id': 1,
            'nombre': 'Sergio',
            'apellido': 'Vaca',
            'años': 20,
            'pais': 'Navi'
        },
        'estudiant 2': {
            'id': 2,
            'nombre': 'Kiara',
            'apellido': 'Reyes',
            'años': 20,
            'pais': 'Chipre'
        },
        'estudiant 3': {
            'id': 3,
            'nombre': 'Petunia',
            'apellido': 'Reyes',
            'años': 8,
            'pais': 'España'
        },
        'estudiant 4': {
            'id': 4,
            'nombre': 'Ryan',
            'apellido': 'Gosling',
            'años': 1,
            'pais': 'Chile'
        }
    }
    msg = {'msg': llistaEstudiants}
    return render(request, 'main_page.html', msg)
def profes(request):
    llistaProfessors = {
        'profe 1':{
            'id': 1,
            'nombre': 'Kike',
            'apellido': 'Vaca',
            'años': 90,
            'pais': 'Guyana'
        },
        'profe 2': {
            'id': 2,
            'nombre': 'Gaby',
            'apellido': 'Cardenas',
            'años': 17,
            'pais': 'Peru'
        },
        'profe 3': {
            'id': 3,
            'nombre': 'Diego',
            'apellido': 'Torres',
            'años': 99,
            'pais': 'Surinam'
        },
        'profe 4': {
            'id': 4,
            'nombre': 'Francisco',
            'apellido': 'Rojas',
            'años': 38,
            'pais': 'Arica'
        }
    }
    msg = {'msg':llistaProfessors}
    return render (request, 'main_page.html', msg)