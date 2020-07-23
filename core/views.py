from django.shortcuts import render, redirect
from core.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
# def index(request):
#    return redirect('/schedule/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid User or Password')
    return redirect('/')


@login_required(login_url='/login/')
def list_events(request):
    user_filter = request.user
    event = Event.objects.filter(users=user_filter)
    data = {'Events': event}
    return render(request, 'schedule.html', data)
