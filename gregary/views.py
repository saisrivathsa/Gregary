from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Event
from .utilities import check_events
from dateutil.parser import parse as parse_date
from datetime import datetime
from django.contrib.auth.models import User
'''
from django.views import generic
from django.db.models import F
'''
def register_event(request):
    try :
        user = User.objects.get(username=request.user.username)
        return render(request, 'gregary/register_event.html')
    except:
        return render(request, 'auth_model/login.html')

def coming_events(request):
    # Deletes the events which ended
    check_events(Event.objects.order_by('start_time'))
    #Gets the list of coming events on basis of start time
    latest_event_list = Event.objects.order_by('start_time')
    context = {'latest_event_list': latest_event_list}
    # Context contains the events' list
    return render(request, 'gregary/coming_events.html', context)

def event_create(request):
    # Checks for valid mobile number and enrollment_number
    if ( len(request.POST['enrollment_number']) != 8 ):
        return render(request, 'gregary/register_event.html', {'error': 'Invalid enrollment number'})
    if ( len(request.POST['phone_number']) != 10 ):
        return render(request, 'gregary/register_event.html', {'error': 'Invalid mobile number'})

        # Creates a new event with the given credentials
    new_event = Event(
        category = request.POST['category'],
        sub_category = request.POST['sub_category'],
        student = request.POST['student'],
        enrollment_number = request.POST['enrollment_number'],
        phone_number = request.POST['phone_number'],
        start_time = request.POST['start_time'],
        end_time = request.POST['end_time']
    )
    # Checks whether the endtime is in the future of start_time
    if(new_event.start_time >= new_event.end_time):
        return render(request, 'gregary/register_event.html', {'error': 'Start time cannot be after end time'})
    # Checks if the end time is not  in the past
    if(parse_date(new_event.end_time) <= datetime.now()):
        return render(request, 'gregary/register_event.html', {'error' : 'Event can\'t end in the past'})
    new_event.save()
    return HttpResponseRedirect(reverse('gregary:coming_events'))
'''
         #for checking left out fields
    for key in request.POST :
        if ( ''== request.POST[key]):
            raise ValueError(key)
    '''#except:
    #        return render(request, 'gregary/register_event.html', {'error': 'Error while handling the form data please fill again'})
    # Saves the event
