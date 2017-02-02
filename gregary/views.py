
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Sport
'''
from django.views import generic
from django.db.models import F
from django.utils import timezone
'''
def index(request):
    return render (request, 'gregary/index.html')

def register_event(request):
    return render(request, 'gregary/register_event.html')

def coming_events(request):
    latest_event_list = Sport.objects.order_by('start_time')
    context = {'latest_event_list': latest_event_list}
    return render(request, 'gregary/coming_events.html', context)

def event_create(request):
    try :
        #if ((request.POST['phone_number']%(10**10) == 0 )):
        #        return render(request, 'gregary/register_event.html', {'error': 'Invalid mobile number'})

        new_event = Sport(
            sub_category = request.POST['sub_category'],
            student = request.POST['student'],
            enrollment_number = request.POST['enrollment_number'],
            phone_number = request.POST['phone_number'],
            start_time = request.POST['start_time'],
            end_time = request.POST['end_time']
        )

        new_event.save()
        return HttpResponseRedirect(reverse('gregary:coming_events'))

    except :
        return render(request, 'gregary/register_event.html', {'error': 'Fill all the required fields'})
