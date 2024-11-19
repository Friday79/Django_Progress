from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        return HttpResponse("You must have POSTed something")
        Else:
        return HttpResponse(request.method)
    
