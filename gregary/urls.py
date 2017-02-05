from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView

app_name = 'gregary'

urlpatterns = [
url(r'^$', TemplateView.as_view(template_name='gregary/index.html'), name='index'),
url(r'^register_event/$', views.register_event, name='register_event'),
url(r'^event_create/$', views.event_create, name='event_create'),
url(r'^events/(?P<cat>[\w\-]+)/$', views.coming_events, name='coming_events'),
url(r'^sample/$', TemplateView.as_view(template_name='gregary/events.html'), name='sample'),
url(r'^home/$', TemplateView.as_view(template_name='gregary/homepage.html'), name='home'),
]
