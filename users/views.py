from django.http import HttpResponse
from django.shortcuts import render


def profile(request, username):
    return HttpResponse('<h1>Профиль</h1>')
