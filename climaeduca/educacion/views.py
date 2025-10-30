from django.http import HttpResponse
from .firebase_config import db
from django.shortcuts import render, redirect
from .forms import RegistroForm
import firebase_admin
from firebase_admin import auth

def prueba(request):
    return render(request, "prueba.html")

def registro_user(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre_usuario']
            correo = form.cleaned_data['correo']
            contraseña = form.cleaned_data['contraseña']
            try:
                user = auth.create_user(
                    email = correo,
                    password = contraseña,
                    display_name = nombre
                )
                return redirect('registro_exitoso')
            except Exception as e:
                return render(request,'registro.html',{'form':form,'error': str(e)})
    else:
        form = RegistroForm()
    return render(request,'registro.html', {'form': form})