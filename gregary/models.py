from __future__ import unicode_literals
from django.db import models

class Event( models.Model ):
    category = models.TextField( default=0, max_length=50, blank=False )
    sub_category = models.TextField( default=0, max_length=50, blank=False )
    start_time = models.DateTimeField( default=0, blank=False )
    end_time = models.DateTimeField( default=0, blank=False )
    student = models.TextField( max_length=50, blank=False, default=0 )
    phone_number = models.IntegerField( default=0, blank=False)
    enrollment_number = models.IntegerField( default=0, blank=False)
