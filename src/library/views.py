from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def library_view(request):
    return HttpResponse("hello library")
