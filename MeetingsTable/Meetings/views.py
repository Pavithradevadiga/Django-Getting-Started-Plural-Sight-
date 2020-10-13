from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Welcome(request):
    return HttpResponse("Welcome to the page")

def About(request):
    return HttpResponse("An effective meeting planner")    