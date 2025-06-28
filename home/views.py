from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


# def home_app(request):
#     return HttpResponse("The wodden spoon home page!")


class Index(TemplateView):
    template_name = 'home/index.html'