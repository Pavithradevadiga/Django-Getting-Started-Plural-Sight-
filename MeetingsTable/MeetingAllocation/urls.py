from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>',views.detail,name = "detail"),
    path('room',views.roomdetail,name="roomdetail"),
    path('newroom',views.new,name="new")
]