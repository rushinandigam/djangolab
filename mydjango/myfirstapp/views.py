from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("<h1>Members Page</h1>")