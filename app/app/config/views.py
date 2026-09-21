from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return HttpResponse("hai :D")

def home(request):
    return render(request, "index.html", {
        "nama": "kevin"
    })