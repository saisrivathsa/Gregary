from django.conf.urls import url, include
from . import views

app_name = 'gregary'

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^auth/', include('auth_model.urls')),
url(r'^register_event/$', views.register_event, name='register_event'),
url(r'^event_create/$', views.event_create, name='event_create'),
url(r'^events/$', views.coming_events, name='coming_events'),
url(r'^vinam_sample/$', views.vinam_sample, name='vinam_sample'),
]
