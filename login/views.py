from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
def login(request):
    t = loader.get_template("login.html")
    return HttpResponse(t.render())