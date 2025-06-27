from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_app(request):
    return HttpResponse("The wodden spoon home page!")