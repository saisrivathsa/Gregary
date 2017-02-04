from .models import Event
from django.utils import timezone

def check_events(latest_event_list):
    for event in latest_event_list:
        if (event.end_time <= timezone.now()):
            event.delete()
