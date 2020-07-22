from django.shortcuts import render, redirect

from core.models import Event

# Create your views here.
#def index(request):
#    return redirect('/schedule/')
def list_events(request):
    event = Event.objects.all()
    data = {'Events': event}
    return render(request, 'schedule.html', data)
