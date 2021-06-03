from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'web/index.html')

def contacto(request):
    return render(request, 'web/contacto.html')

def login(request):
    return render(request, 'web/login.html')

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

    