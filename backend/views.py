from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request, "backend/index.html")


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Inscription réussie!")
            return redirect("login")
        messages.warning(request, "Erreur d'enregistrement. Des informations semblent invalides.")
    form = NewUserForm()
    return render(request, template_name="registration/register.html", context={"register_form": form})


def view_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Bienvenue, {username}.")
                return redirect("home")
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe invalide.")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe invalide.")
    form = AuthenticationForm()
    return render(request, template_name="registration/login.html", context={"login_form": form})


def view_logout(request):
    logout(request)
    messages.info(request, "Vous êtes déconnecté.")
    return redirect("home")
