# Django Libraries
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Models
from .models import Articles, Subscription
from .util import *


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "POST":
        email = request.POST["email"]
        try:
            subscribe = Subscription.objects.create(email=email)
            subscribe.save()
            messages.add_message(request, messages.SUCCESS, "Subscribed Successfully.")
        except IntegrityError:
            messages.add_message(request, messages.ERROR, "Already Subscribed!")
    return render(request, "trader/index.html")


def about(request):
    return render(request, "trader/about.html")


def contact(request):
    return render(request, "trader/contact.html")


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

    return render(request, "trader/blog-home.html")
