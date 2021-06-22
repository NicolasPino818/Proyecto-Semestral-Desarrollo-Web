from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    #contacto mensaje
    path("contacto/", views.contacto , name="contacto"), #agregar
    path("contactcrud/", views.contactcrud , name="contactcrud"), #listar
    path("lcontdel/<iduserc>/", views.lcontdel , name="lcontdel"), #eliminar
    # fin contacto mensaje
    path("login/", views.login, name="login"),
    path("stock/", views.stock, name="stock"),
    path("modelo/", views.modelo, name="modelo"),
    path("nosotros/", views.nosotros , name="nosotros"),
    #producto
    path("addproducto/", views.addproducto, name='addproducto'), #agregar
    path("productcrud/", views.productcrud, name='productcrud'), #listar
    path("deleteproduct/<idproduct>/", views.deleteproduct, name="deleteproduct"), #eliminar
    path("editproduct/<idproduct>", views.editproduct, name="editproduct"), ##editar

    path("productos/", views.productos, name='productos'),
    path("ropahombre/", views.ropahombre, name="ropahombre"),
    path("ropamujer/", views.ropamujer , name="ropamujer"),
    path("ropanina/", views.ropanina, name="ropanina"),
    path("ropanino/", views.ropanino, name="ropanino"),
    #crud uuario
    path("userscrud/", views.userscrud, name="userscrud"), #listar
    path("eliminar/<iduser>/", views.eliminar, name="eliminar"), #eliminar
    path("register/", views.registro, name="register"), #registrar
    #fin creliminarud
    path("adduseradmin/", views.adduseradmin, name="adduseradmin"),
    path("edituser/<iduser>", views.edituser, name="edituser"),
]