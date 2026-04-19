from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy


@login_required(login_url=("core:login"))
def home(request):
    context = {"name": "home page"}
    return render(request, "core/home.html", context)


# --- REGISTER VIEW ---
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Register hote hi login karwa do
            messages.success(request, "Registration Successful!")
            return redirect("core:home")
    else:
        form = UserCreationForm()
    return render(request, "core/register.html", {"form": form})


# --- LOGIN VIEW ---
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("core:home")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "core/login.html", {"form": form})


# --- LOGOUT VIEW ---
def logout_view(request):
    logout(request)
    messages.info(request, "You have logged out.")
    return redirect("core:login")


class Login(LoginView):
    template_name = "core/login.html"
    next_page = "core:home"


class Logout(LogoutView):
    next_page = "core:login"


class Register(CreateView):
    form_class = UserCreationForm
    template_name = "core/register.html"
    success_url = reverse_lazy("core:login")
