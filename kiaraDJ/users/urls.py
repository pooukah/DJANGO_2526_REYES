from django.urls import path
from . import views

urlpatterns = [
    path("profes", views.profes, name="professors"),
    path("estudiants", views.estudiants, name="estudiants")
]