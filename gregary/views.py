from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Sport
from django.utils import timezone
'''
from django.views import generic
from django.db.models import F
'''

def coming_events(request):
    latest_event_list = Sport.objects.order_by('start_time')
    context = {'latest_event_list': latest_event_list}
    return render(request, 'gregary/coming_events.html', context)

def event_create(request):
    try :
        if ( len(request.POST['enrollment_number']) != 8 ):
            return render(request, 'gregary/register_event.html', {'error': 'Invalid enrollment number'})
        if ( len(request.POST['phone_number']) != 10 ):
            return render(request, 'gregary/register_event.html', {'error': 'Invalid mobile number'})
        new_event = Sport(
            sub_category = request.POST['sub_category'],
            student = request.POST['student'],
            enrollment_number = request.POST['enrollment_number'],
            phone_number = request.POST['phone_number'],
            start_time = request.POST['start_time'],
            end_time = request.POST['end_time']

        )
        if(new_event.start_time >= new_event.end_time):
            return render(request, 'gregary/register_event.html', {'error': 'Start time cannot be after end time'})
        if(new_event.end_time <= timezone.now()):
            return render(request, 'gregary/register_event.html', {'error' : 'Event can\'t end in the past'})
        new_event.save()
        return HttpResponseRedirect(reverse('gregary:coming_events'))

    except:
        return render(request, 'gregary/register_event.html', {'error': 'Fill all the required fields'})
