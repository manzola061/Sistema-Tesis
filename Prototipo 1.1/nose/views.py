from django.shortcuts import render, redirect
from .models import Camionero
from .models import Camion
from .forms import CamioneroForm
from .forms import CamionForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')  # Redirigir al inicio tras iniciar sesión
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def inicio(request):
    return render(request, 'paginas/inicio.html')

@login_required
def camioneros(request):
    camioneros = Camionero.objects.all()
    return render(request, 'camioneros/index.html', {'camioneros': camioneros})

@login_required
def crear(request):
    formulario = CamioneroForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('camioneros')
    return render(request, 'camioneros/crear.html', {'formulario': formulario})

@login_required
def editar(request, cedula):
    camionero = Camionero.objects.get(cedula=cedula)
    formulario = CamioneroForm(request.POST or None, instance=camionero)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('camioneros')
    return render(request, 'camioneros/editar.html', {'formulario': formulario})

@login_required
def borrar(request, cedula):
    camionero = Camionero.objects.get(cedula=cedula)
    camionero.delete()
    return redirect('camioneros')

@login_required
def camiones(request):
    camiones = Camion.objects.all()
    return render(request, 'camiones/index_camion.html', {'camiones': camiones})

@login_required
def crear_camion(request):
    formulario = CamionForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('camiones')
    return render(request, 'camiones/crear_camion.html', {'formulario': formulario})

@login_required
def editar_camion(request, placa):
    camion = Camion.objects.get(placa=placa)
    formulario = CamionForm(request.POST or None, instance=camion)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('camiones')
    return render(request, 'camiones/editar_camion.html', {'formulario': formulario})

@login_required
def borrar_camion(request, placa):
    camion = Camion.objects.get(placa=placa)
    camion.delete()
    return redirect('camiones')
