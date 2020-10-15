from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Meeeting

def detail(request,id):
    meeting = get_object_or_404(Meeeting, pk=id)
    return render(request,"MeetingAllocation/detail.html",{"meeting":meeting})