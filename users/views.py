# Django Libraries
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.db import IntegrityError
from django.contrib import messages

from .models import User


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("trader:index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid username and/or password."
            })
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("trader:index"))


def register(request):
    if request.user.is_authenticated:
        # must redirect to market panel
        return HttpResponseRedirect(reverse("trader:index"))

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if len(username) == 0:
            messages.add_message(request, messages.INFO, "Username is not entered!")

        if len(password) == 0:
            messages.add_message(request, messages.INFO, "Password is not entered!")

        if len(email) == 0:
            messages.add_message(request, messages.INFO, "Email is not entered!")

        if password != confirmation:
            messages.add_message(request, messages.WARNING, "Passwords must match!")

        if messages:
            return render(request, "users/register.html")

        try:
            user = User.objects.create_user(username, email, password)
            # user.save()
        except IntegrityError:
            messages.add_message(request, messages.ERROR, "Username already taken!")
            return render(request, "users/register.html")

        login(request, user)
        return HttpResponseRedirect(reverse("trader:index"))
    return render(request, "users/register.html")
