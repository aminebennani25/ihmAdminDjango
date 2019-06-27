from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def affiche(request):
    return HttpResponse("HELLO !")
