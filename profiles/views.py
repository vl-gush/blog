from django.http import HttpResponse
import logging
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from profiles.forms import RegisterForm


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
