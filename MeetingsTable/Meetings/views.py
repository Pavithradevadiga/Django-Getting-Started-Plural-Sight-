from django.shortcuts import render
from django.http import HttpResponse
from MeetingAllocation.models import Meeeting

# Create your views here.
def Welcome(request):
    return render(request,"Meetings/welcome.html",
    {"meetings" : Meeeting.objects.all()})
def About(request):
    return HttpResponse("An effective meeting planner")    