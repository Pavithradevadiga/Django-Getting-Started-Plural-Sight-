from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Meeeting,Room

def detail(request,id):
    meeting = get_object_or_404(Meeeting, pk=id)
    return render(request,"MeetingAllocation/detail.html",{"meeting":meeting})

def roomdetail(request):
    return render(request,"MeetingAllocation/roomdetail.html",{"rooms":Room.objects.all()})
