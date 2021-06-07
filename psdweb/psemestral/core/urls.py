from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
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
    #crud
    path("userscrud/", views.userscrud, name="userscrud"),
    path("eliminar/<iduser>/", views.eliminar, name="eliminar"),
    #fin creliminarud
    path("adduseradmin/", views.adduseradmin, name="adduseradmin"),
    path("register/", views.register, name="register"),
]