from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from .models import user, usercontact, newProduct
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
        #mensaje = "No se puedo enviar el mensaje, revisa los datos"
        #messages.error(request, mensaje)

    return render(request, 'web/contacto.html', data)

def contactcrud(request): #listar
    contacts = usercontact.objects.all()
    users = user.objects.all()
    products = newProduct.objects.all()
    numproducts = products.count()
    numusers = users.count()
    numcontacts = contacts.count()
    data = {
        'ucontacts' : contacts, 'nusers' : numusers, 'ncontacts' : numcontacts, 'nproducts' : numproducts
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

# CRUD Producto

def stock(request): #listar producto en crud
    product = newProduct.objects.all()

    data = {
        'product' : product
    }
    return render(request, 'web/stock.html', data)


def addproducto(request): #AGREGAR PRODUCTO
    
    data = {'proForm' : addProduct()}
    if request.method == 'POST':
        product = addProduct(data = request.POST) 
        if product.is_valid():
            product.save()
            print("producto Creado Correctamente")
            data['message'] = "Producto agregado y guardado correctamente"
            mensaje = "producto Creado Correctamente"
            messages.success(request, mensaje)
            return redirect('addproducto')
        else:
            data["proForm"] = product;  
    else:
        print("No se puedo crear el producto, revisa los datos")
        data['message'] = "Producto NO agregado"
        mensaje = "No se puedo crear el producto, revisa los datos"
        messages.error(request, mensaje)
    return render(request, 'web/addproducto.html', data)

def productcrud(request): #listar producto en crud
    users = user.objects.all()
    contacts = usercontact.objects.all()
    products = newProduct.objects.all()

    numusers = users.count()
    numcontacts = contacts.count()
    numproducts = products.count()
    data = {
        'product' : products, 'nusers' : numusers, 'ncontacts' : numcontacts, 'nproducts' : numproducts
    }
    return render(request, 'web/productcrud.html', data)

def editproduct(request, idproduct): #editar producto desde un administrador
    eproduct = newProduct.objects.get(id=idproduct)
    data = {
    'form': addProduct(instance=eproduct) 
    }
    if request.method == 'POST':
        formulario_edit = addProduct(data=request.POST, instance=eproduct)
        if formulario_edit.is_valid:
            formulario_edit.save()
            data['mensaje'] = "producto editado correctamente"
            return redirect('productcrud')
        else:
            data["fomr"] = formulario_edit;  
    return render(request, 'web/editproduct.html', data)

def deleteproduct(request, idproduct): #eliminar usuario desde un adminw
    product = newProduct.objects.get(id=idproduct)

    try:
        newProduct.delete(product)
        print("Producto Eliminado Correctamente")
        mensaje = "Producto Eliminado Correctamente"
        messages.success(request, mensaje)
        
    except:
        print('No se puedo eliminar, revisa los datos')
        mensaje = "No se puedo eliminar, revisa los datos"
        messages.error(request, mensaje)
        
    return redirect('productcrud')



def productos(request):
    return render(request, 'web/productos.html')    

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
#stock
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
    products = newProduct.objects.all()
    numproducts = products.count()
    numusers = users.count()
    numcontacts = contacts.count()
    data = {
        'users' : users, 'nusers' : numusers, 'ncontacts' : numcontacts, 'nproducts' : numproducts
    }
    return render(request, 'web/userscrud.html', data)

# fin funciones para el crud


#status

    


    