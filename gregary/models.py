from __future__ import unicode_literals
from django.db import models

class Event( models.Model ):
    category = models.TextField( default=None, max_length=50, blank=False )
    sub_category = models.TextField( default=None, max_length=50, blank=False )
    start_time = models.DateTimeField( default=None, blank=False )
    end_time = models.DateTimeField( default=None, blank=False )
    student = models.TextField( max_length=50, blank=False, default=None )
    phone_number = models.IntegerField( default=None, blank=False)
    enrollment_number = models.IntegerField( default=None, blank=False)
