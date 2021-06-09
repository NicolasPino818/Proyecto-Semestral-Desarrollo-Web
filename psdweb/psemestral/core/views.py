from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from .models import user, usercontact
from .forms import contactForm, registroUser
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'web/index.html')


# funciones para el coontacto
def contacto(request): #agregar

    msnform = contactForm()
    data = {'cform' : msnform}
    
    if request.method == 'POST':
        msnform = contactForm(data = request.POST) 
        if msnform.is_valid():
            msnform.save()
        else:
            data["cform"] = msnform;
        
        print("Mensaje enviado Correctamente")
        mensaje = "Mensaje enviado Correctamente"
        messages.success(request, mensaje)
    else:
        print("No se puedo enviar el mensaje, revisa los datos")
        mensaje = "No se puedo enviar el mensaje, revisa los datos"
        messages.error(request, mensaje)

    return render(request, 'web/contacto.html', data)

def contactcrud(request): #listar
    contacts = usercontact.objects.all()
    data = {
        'ucontacts' : contacts
    }
    return render(request, 'web/contactcrud.html', data)

def lcontdel(request, iduserc): #eliminar
    contacts = usercontact.objects.get(id=iduserc)

    try:
        usercontact.delete(contacts)
        print("Eliminado Correctamente")
        mensaje = "Eliminado Correctamente"
        messages.success(request, mensaje)
        
    except:
        print("No se puedo eliminar, revisa los datos")
        mensaje = "No se puedo eliminar, revisa los datos"
        messages.error(request, mensaje)
        
    return redirect('contactcrud')
    

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

def userscrud(request): #listar
    users = user.objects.all()
    data = {
        'users' : users
    }
    return render(request, 'web/userscrud.html', data)

def eliminar(request, iduser): #eliminar
    users = user.objects.get(id=iduser)

    try:
        user.delete(users)
        print("Eliminado Correctamente")
        mensaje = "Eliminado Correctamente"
        messages.success(request, mensaje)
        
    except:
        print("No se puedo eliminar, revisa los datos")
        mensaje = "No se puedo eliminar, revisa los datos"
        messages.error(request, mensaje)
        
    return redirect('userscrud')

def registro(request):

    reguser = registroUser()
    data = {'reguform' : reguser}
    
    if request.method == 'POST':
        reguser = contactForm(data = request.POST) 
        if reguser.is_valid():
            reguser.save()
            return redirect('register')
        else:
            data["reguform"] = reguser;
        
        print("Usuario Creado Correctamente")
        mensaje = "Usuario Creado Correctamente"
        messages.success(request, mensaje)
    else:
        print("No se puedo crear el usuario, revisa los datos")
        mensaje = "No se puedo crear el usuario, revisa los datos"
        messages.error(request, mensaje)

    return render(request, 'web/register.html', data)

# fin funciones para el crud

def adduseradmin(request):
    return render(request, 'web/adduseradmin.html')

def login(request):
    return render(request, 'web/login.html')


    