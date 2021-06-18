from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from .models import user, usercontact 
from .forms import contactForm, registroUser, addProduct
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
    users = user.objects.all()
    numusers = users.count()
    numcontacts = contacts.count()
    data = {
        'ucontacts' : contacts, 'nusers' : numusers, 'ncontacts' : numcontacts
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

# End funciones para el coontacto

def modelo(request):
    return render(request, 'web/modelo.html')

def nosotros(request):
    return render(request, 'web/nosotros.html')

def addproducto(request):
    
    product = addProduct()
    data = {'proForm' : product}
    if request.method == 'POST':
        product = registroUser(data = request.POST) 
        if product.is_valid():
            product.save()
            print("producto Creado Correctamente")
            mensaje = "producto Creado Correctamente"
            messages.success(request, mensaje)
            return redirect('producto')
        else:
            data["reguform"] = product;  
    else:
        print("No se puedo crear el producto, revisa los datos")
        mensaje = "No se puedo crear el producto, revisa los datos"
        messages.error(request, mensaje)

    return render(request, 'web/addproducto.html', data)


def stock(request):
    return render(request, 'web/stock.html')    

def ropahombre(request):
    return render(request, 'web/ropahombre.html')

def ropamujer(request):
    return render(request, 'web/ropamujer.html')

def ropanina(request):
    return render(request, 'web/ropanina.html')

def ropanino(request):
    return render(request, 'web/ropanino.html')

#login and register by user

def registro(request): #registro user

    reguser = registroUser()
    data = {'reguform' : reguser}
    if request.method == 'POST':
        reguser = registroUser(data = request.POST) 
        if reguser.is_valid():
            reguser.save()
            print("Usuario Creado Correctamente")
            mensaje = "Usuario Creado Correctamente"
            messages.success(request, mensaje)
            return redirect('index')
        else:
            data["reguform"] = reguser;  
    else:
        print("No se puedo crear el usuario, revisa los datos")
        mensaje = "No se puedo crear el usuario, revisa los datos"
        messages.error(request, mensaje)

    return render(request, 'web/register.html', data)

def login(request):
    return render(request, 'web/login.html')
    


# End login and register by user

#funciones para el crud

def adduseradmin(request): #registro de usuario para un administrador
    reguser = registroUser()
    data = {'addform' : reguser}
    if request.method == 'POST':
        reguser = registroUser(data = request.POST) 
        if reguser.is_valid():
            reguser.save()
            print("Usuario Creado Correctamente")
            mensaje = "Usuario Creado Correctamente"
            messages.success(request, mensaje)
            return redirect('userscrud')
        else:
            data["addform"] = reguser;  
    else:
        print("No se puedo crear el usuario, revisa los datos")
        mensaje = "No se puedo crear el usuario, revisa los datos"
        messages.error(request, mensaje)
    return render(request, 'web/adduseradmin.html', data)

def edituser(request, iduser): #editar usuario desde un administrador
    euser = user.objects.get(id=iduser)
    data = {
    'form': registroUser(instance=euser) 
    }
    if request.method == 'POST':
        formulario_edit = registroUser(data=request.POST, instance=euser)
        if formulario_edit.is_valid:
            formulario_edit.save()
            data['mensaje'] = "usuario editado correctamente"
            return redirect('userscrud')
        else:
            data["fomr"] = formulario_edit;  
    return render(request, 'web/edituser.html', data)

def eliminar(request, iduser): #eliminar usuario desde un adminw
    users = user.objects.get(id=iduser)

    try:
        user.delete(users)
        print("Eliminado Correctamente")
        mensaje = "Eliminado Correctamente"
        messages.success(request, mensaje)
        
    except:
        print('No se puedo eliminar, revisa los datos')
        mensaje = "No se puedo eliminar, revisa los datos"
        messages.error(request, mensaje)
        
    return redirect('userscrud')


def userscrud(request): #listar
    users = user.objects.all()
    contacts = usercontact.objects.all()

    numusers = users.count()
    numcontacts = contacts.count()
    data = {
        'users' : users, 'nusers' : numusers, 'ncontacts' : numcontacts
    }
    return render(request, 'web/userscrud.html', data)

# fin funciones para el crud


#status

    


    