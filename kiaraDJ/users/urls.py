from django.urls import path
from . import views

urlpatterns = [
    path("profes/", views.profes, name="professors"),
    path("estudiants/", views.estudiants, name="estudiants"),
    path("all/", views.all),
    path("unUsuari/<int:pk>", views.unUsuari)
]