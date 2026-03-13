from django.urls import path
from . import views

urlpatterns = [
    path("profes/", views.profes, name="professors"),
    path("estudiants/", views.estudiants, name="estudiants"),
    path("usuaris/", views.all, name="usuaris"),
    path("unUsuari/<int:pk>", views.unUsuari, name="usuarisPK")
]