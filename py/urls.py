#las URLS para importar algun que otro objeto
from django.urls import path
from .views import ropa-hombre, ropa-hombres, ropa-mujer, ropa-mujeres, ropa-ninas, ropa-nina, ropa-ninos, ropa-nino
from .viewsLogin import login

urlpatterns = [
  path('ropa hombre/', ropa-hombres, name="ropa de hombres"),
  path('ropa hombre/<pk>', ropa-hombre, name="ropa de hombre"),
  path('ropa mujer/', ropa-mujeres, name="ropa de mujeres"),
  path('ropa mujer/<pk>', ropa-mujer, name="ropa de mujer"),
  path('ropa nina/', ropa-ninas, name="ropa de niñas"),
  path('ropa nina/<pk>', ropa-nina, name="ropa de niña"),
  path('ropa nino/', ropa-ninos, name="ropa de niños"),
  path('ropa nino/<pk>', ropa-nino, name="ropa de niño"),
  path('login/', login, name='login'),
]
