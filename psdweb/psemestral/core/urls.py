from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("contacto/", views.contacto , name="contacto"),
    path("login/", views.login, name="login"),
    path("modelo/", views.modelo, name="modelo"),
    path("nosotros/", views.nosotros , name="nosotros"),
    path("productos/", views.productos, name="productos"),
    path("ropahombre/", views.ropahombre, name="ropahombre"),
    path("ropamujer/", views.ropamujer , name="ropamujer"),
    path("ropanina/", views.ropanina, name="ropanina"),
    path("ropanino/", views.ropanino, name="ropanino"),
]