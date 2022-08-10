from django.http import HttpResponse
import logging
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate

from profiles.forms import RegisterForm, LoginForm


logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def profiles(request):
    message = []
    for key, value in request.GET.items():
        message.append(f'{key} = {value}')

    if len(request.POST):
        for key, value in request.POST.items():
            logger.info(f"{key} = {value}")

    if len(message):
        return HttpResponse(f"Profile view with GET params: {', '.join(message)}")
    return HttpResponse("Profile view")


def register(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                email=form.cleaned_data["email"],
                username=form.cleaned_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
            )
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request=request, **form.cleaned_data)
            if user is None:
                return HttpResponse('BadRequest', status=400)
            login(request, user)
            return redirect("index")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")
