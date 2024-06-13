from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
def signup(request):
    t = loader.get_template("signup.html")
    return HttpResponse(t.render())
