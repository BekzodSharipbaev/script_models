from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import SiteUser, Song, Concert

# Create your views here.
def home(request):
    return render(request, "home.html")


def users(request):
    context = {'model_name': 'users',
               'data': SiteUser.objects.all(),
               }
    return render(request, "models.html", context)


def songs(request):
    context = {'model_name': 'songs',
               'data': Song.objects.all(),
               }
    return render(request, "models.html", context)


def concerts(request):
    context = {'model_name': 'concerts',
               'data': Concert.objects.all(),
               }
    return render(request, "models.html", context)



