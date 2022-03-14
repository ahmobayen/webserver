# Django Libraries
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt

# Models
from .models import User, Articles
from .util import *

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "POST":
        print(request.POST["email"])
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.user.is_authenticated:
        # must redirect to market panel
        return HttpResponseRedirect(reverse("index"))

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        message = ""

        if len(username) == 0:
            message = message + "Username is not entered \n"

        if len(password) == 0:
            message = message + "Password is not entered \n"

        if len(email) == 0:
            message = message + "Email is not entered \n"
        if password != confirmation:
            message = message + "Passwords must match"

        if len(message) != 0:
            print(message)
            return render(request, "register.html", {
                "message": message,
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "register.html")


def articles(request):
    if "query" in request.GET.keys():
        try:
            number_of_posts = int(request.GET["query"])
        except ValueError:
            number_of_posts = 3

        posts = [post.serialize() for post in Articles.objects.all().order_by('-timestamp')[:number_of_posts]]
        return JsonResponse(posts, safe=False)

    if "page" in request.GET.keys():
        page_number = int(request.GET["page"])
        posts = Articles.objects.all().order_by('-timestamp')
        p = Paginator(posts, 15)

        if page_number > p.num_pages:
            return JsonResponse({'status': 'false', 'message': 'No more content to load'}, status=404)

        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)

        data = [post.serialize() for post in page_obj]
        page_info = {"current_page": page_number,
                     "number_of_pages": p.num_pages}
        data.append(page_info)
        return JsonResponse(data, safe=False)

    return render(request, "blog-home.html")
