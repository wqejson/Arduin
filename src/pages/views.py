from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {'title': 'about'})


def service_view(request, *args, **kwargs):
    return render(request, "service.html", {'title': 'offers'})


# Create your views here.
