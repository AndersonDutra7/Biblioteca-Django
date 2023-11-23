from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login


def user_login(request):
    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")

        if not all([user, password]):
            messages.error(request, "Favor, preencha todos os campos.")
            return redirect("login")

        user = authenticate(request, username=user, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Usuário ou senha incorretos.")
            return redirect("login")
    else:
        return render(request, "pages/login.html")


def register(request):
    if request.method == "POST":
        user = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        passwordConfirm = request.POST.get("password-confirm")

        if not all([user, email, password, passwordConfirm]):
            messages.error(request, "Favor, preencha todos os campos.")
            return redirect("register")

        if password != passwordConfirm:
            messages.error(request, "As senhas não coincidem.")
            return redirect("register")

        try:
            User.objects.create_user(username=user, email=email, password=password)
            messages.success(request, "Conta criada com sucesso.")
            messages.success(request, "Faça o login.")
            return redirect("login")

        except IntegrityError as e:
            if "UNIQUE constraint failed: auth_user.username" in str(e):
                messages.error(request, "Nome de usuário existente.")
            elif "UNIQUE constraint failed: auth_user.email" in str(e):
                messages.error(request, "Nome de usuário existente.")
            else:
                messages.error(request, "Erro ao criar a conta.")

    return render(request, "pages/register.html")


def logout(request):
    auth.logout(request)
    return redirect("login")
