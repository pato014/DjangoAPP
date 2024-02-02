from django.shortcuts import render
from .models import Room, Comments

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(requst, pk):
    room = Room.objects.get(id=pk)
    comments = Comments.objects.all()
    context = {'room': room,
               "comments": comments}
    return render(requst, 'base/rooms.html', context)
