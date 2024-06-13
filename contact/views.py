from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def contact(request):
    t = loader.get_template("contact.html")
    return HttpResponse(t.render())
