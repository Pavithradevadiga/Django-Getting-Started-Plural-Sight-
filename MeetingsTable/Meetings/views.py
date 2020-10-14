from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Welcome(request):
    return render(request,"Meetings/welcome.html",
    {"message" : "To check if template variable is working fine"}
    )

def About(request):
    return HttpResponse("An effective meeting planner")    