from django.shortcuts import render, redirect
from .models import user
from .forms import contactForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'web/index.html')

def contacto(request):
    return render(request, 'web/contacto.html')

def register(request):
    data = {
        'form' : contactForm()
    }
    return render(request, 'web/register.html', data)

def modelo(request):
    return render(request, 'web/modelo.html')

def nosotros(request):
    return render(request, 'web/nosotros.html')

def productos(request):
    return render(request, 'web/productos.html')

def ropahombre(request):
    return render(request, 'web/ropahombre.html')

def ropamujer(request):
    return render(request, 'web/ropamujer.html')

def ropanina(request):
    return render(request, 'web/ropanina.html')

def ropanino(request):
    return render(request, 'web/ropanino.html')

#funciones para el crud

def userscrud(request):
    users = user.objects.all()
    data = {
        'users' : users
    }
    return render(request, 'web/userscrud.html', data)

def eliminar(request, iduser):
    users = user.objects.get(id=iduser)

    try:
        user.delete(users)
        print("Eliminado Correctamente")
        
    except:
        print("No se puedo eliminar, revisa los datos")
        
    return redirect('userscrud')

# fin funciones para el crud

def adduseradmin(request):
    return render(request, 'web/adduseradmin.html')

def login(request):
    return render(request, 'web/login.html')


    