# from django.shortcuts import render
from django.http import HttpResponse

#this is the function used to create the hhtp response for /polls
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


