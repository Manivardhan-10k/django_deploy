from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def welcome(req):
    return HttpResponse("response from deployment")