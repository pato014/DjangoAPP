from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.db.models import Q
from .models import Room, Comments, Topic
from .forms import RoomForm

# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username doesn't exist")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password doesn't exists")

    context = {}
    return render(request, 'base/login_register.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('query') if request.GET.get('query') != None else ''
    # rooms = Room.objects.filter(topic__name__icontains=q)
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__contains=q)
    )
    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'base/home.html', context)


def room(requst, pk):
    room = Room.objects.get(id=pk)
    comments = Comments.objects.all()
    context = {'room': room,
               "comments": comments}
    return render(requst, 'base/rooms.html', context)

@login_required()
def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form': form}
    return render(request, 'base/room_form.html', context)
@login_required()
def update_room(request, pk):
    room = Room.objects.get(id=pk)

    form = RoomForm(instance=room)
    if request.user != room.host:
        return HttpResponse('You are not owner of this room')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        form.save()
        return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required()
def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('You are not owner of this room')
    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'object': room})

