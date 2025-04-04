from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegistroForm, LoginForm


def registro_view(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        # ? Valida que el formulario sea válido y que el usuario no exista
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso.")
            return redirect("home")

        # ! El formulario no es válido o el usuario ya existe
        messages.error(request, "Registro fallido. Información inválida.")
    else:
        form = RegistroForm()
    return render(request, "auth/registro.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        # ? Valida que el formulario sea válido y que el usuario exista
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            # ! El usuario no existe
            if not user:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
                return redirect("login")

            login(request, user)
            messages.info(request, f"Has iniciado sesión como {username}.")
            return redirect("home")  # Asegúrate de que esta URL exista

        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = LoginForm()
    return render(request, "auth/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect("home")  # Asegúrate de que esta URL exista
