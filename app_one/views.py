from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from time import gmtime, strftime


def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, "index.html", context)


def route_one(request):
    return redirect("/")


def route_two(request, name):
    context = {
        "name": name
    }
    return render(request, "template2.html", context)


def route_three(request):
    return JsonResponse({"content": "lorem ipsum", "status": True})
